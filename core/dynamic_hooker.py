import frida

from core import sandbox


class DynamicHooker:
    """对应'Frida script injection'"""

    def __init__(self, sandbox):
        self.sandbox = sandbox
        self.pid = self._get_container_pid()

    def _get_container_pid(self):
        """获取容器内进程PID"""
        top_output = self.sandbox.container.top()
        return top_output["Processes"][0][1]  # 提取第一个进程PID

    def inject(self):
        self.session = frida.attach(self.pid)
        """注入挂钩脚本"""
        script = """
        Interceptor.attach(Module.getExportByName('ws2_32.dll', 'connect'), {
            onEnter: function(args) {
                var sockaddr = args[1];
                var ip = sockaddr.add(4).readByteArray(4);
                var port = sockaddr.add(2).readU16();
                send({type: 'c2_config', data: {ip: ip, port: port}});
            }
        });
        """
        self.script = self.session.create_script(script)
        self.script.on('message', self.on_message)
        self.script.load()

    def on_message(self, message, _):
        if message['type'] == 'c2_config':
            print("[*] 捕获动态配置:", message['data'])
