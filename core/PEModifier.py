
class PEModifier:
    def __init__(self, input_file, output_file):
        self.input = input_file
        self.output = output_file

    # 读取PE文件并且将IP地址和端口内容修改
    def modify_pe_hex_string(self, start_addr, end_addr, bytes_provided):

        # try:
        #     new_bytes = bytes.fromhex(new_hex_string)
        # except ValueError as e:
        #     print(f"无效的十六进制字符串: {e}")
        #     return

        # 计算需要修改的长度
        original_length = end_addr - start_addr
        new_length = len(bytes_provided)

        if new_length != original_length:
            print(f"警告: 新数据长度({new_length})与原数据长度({original_length})不同")
            # 可以选择截断或填充，这里简单处理为拒绝
            print("新数据长度必须与原数据长度相同")
            return

        # 读取并修改文件
        try:
            with open(self.input, 'rb') as f:
                data = bytearray(f.read())

            # 检查地址是否有效
            if start_addr < 0 or end_addr >= len(data):
                print("错误: 指定的地址范围超出文件大小")
                return

            # 替换数据
            data[start_addr:end_addr] = bytes_provided

            # 写入新文件
            with open(self.output, 'wb') as f:
                f.write(data)

            print(f"成功修改并保存到 {self.output}")

        except Exception as e:
            print(f"处理文件时出错: {e}")