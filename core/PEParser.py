import re

from model.Info import Info


class PEParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ips = []
        self.ports = []

    # 从文件中解析出ip和端口内容
    def extract_config(self):
        with open(self.file_path, 'rb') as f:
            data = f.read()
            for ip_match in re.finditer(b"\xAC\x1B\x2C\xBA", data):
                print(f"ip offset: {ip_match.start()}")
                info = Info(ip_match.start(), ip_match.end())
                self.ips.append(info)

            for port_match in re.finditer(b"\x11\\x5C", data):
                print(f"port offset: {port_match.start()}")
                info = Info(port_match.start(), port_match.end())
                self.ports.append(info)
