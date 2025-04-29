import pefile
import re


class PEParser:
    """对应流程图中的'Parse module of PE file'"""

    def __init__(self, file_path):
        self.pe = pefile.PE(file_path)

    def extract_config(self):
        """提取IP/端口配置"""
        for section in self.pe.sections:
            if b".rdata" in section.Name:
                data = section.get_data()
                # 匹配IP地址 (如192.168.1.1)
                ip_match = re.search(b'\xAC\x1B\x2C\xBA', data)
                if ip_match:
                    return {
                        'ip': ip_match.group().decode(),
                        'port': int.from_bytes(data[ip_match.end():ip_match.end() + 2], 'little')
                    }
        return None