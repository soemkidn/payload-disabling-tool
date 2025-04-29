from core.pe_parser import PEParser
from core.dynamic_hooker import DynamicHooker
from core.patcher import Patcher
import sys
import queue


def wait_for_dynamic_config(timeout=30):
    """
    动态配置等待逻辑
    :param timeout: 最大等待秒数
    :return: 捕获的配置字典或None
    """
    # 创建线程安全队列
    config_queue = queue.Queue(maxsize=1)

    # 重写DynamicHooker的回调方法
    def on_message(message, _):
        if message.get('type') == 'c2_config':
            config_queue.put(message['data'])

    # 启动动态挂钩
    hooker = DynamicHooker("malware.exe")
    hooker.script.on('message', on_message)
    hooker.inject()

    # 主线程等待结果
    try:
        return config_queue.get(timeout=timeout)
    except queue.Empty:
        print("[!] 动态分析超时，未捕获配置")
        return None
    finally:
        hooker.session.detach()

def main(input_file, output_file):
    # 1. PE解析
    parser = PEParser(input_file)
    config = parser.extract_config()

    # 2. 配置定位策略
    if not config:  # 静态分析失败时转动态
        print("[!] 静态分析未发现配置，启动动态挂钩...")
        hooker = DynamicHooker(input_file)
        hooker.inject()
        config = wait_for_dynamic_config()  # 需实现等待逻辑

    # 3. 修改配置
    patcher = Patcher(input_file)
    patcher.patch(config['ip'], config['port'])

    # 4. 输出结果
    patcher.save(output_file)
    print(f"[+] 阻断完成: {output_file}")


if __name__ == "__main__":
    main('payload.exe', 'blocked_payload.exe')