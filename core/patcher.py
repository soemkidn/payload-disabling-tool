import pefile


class Patcher:
    """对应'IP address/Port replacement'和'Examination'"""

    def __init__(self, input_file):
        with open(input_file, 'rb') as f:
            self.data = bytearray(f.read())

    def patch(self, old_ip, new_ip="127.0.0.1", old_port=None, new_port=0):
        """二进制补丁"""
        # IP替换
        self.data = self.data.replace(
            bytes(map(int, old_ip.split('.'))),
            bytes(map(int, new_ip.split('.')))
        )
        # 端口替换
        if old_port:
            self.data = self.data.replace(
                old_port.to_bytes(2, 'little'),
                new_port.to_bytes(2, 'little')
            )

    def save(self, output_file):
        """保存并校验"""
        pe = pefile.PE(data=self.data)
        pe.OPTIONAL_HEADER.CheckSum = pe.generate_checksum()
        pe.write(output_file)
        pe.close()