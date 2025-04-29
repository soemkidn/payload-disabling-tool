import os


class PEFileViewer:
    def __init__(self, file_path):
        """
        初始化PE文件查看器
        :param file_path: PE文件路径
        """
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件 {file_path} 不存在")

    # 查看指定地址范围的十六进制内容
    def view_hex_range(self, start_addr, end_addr):
        """
        查看指定地址范围的十六进制内容
        :param start_addr: 开始地址(十进制)
        :param end_addr: 结束地址(十进制)
        :return: 十六进制字符串(如 b'\x7C\x00')
        """
        # 验证地址范围
        if start_addr < 0 or end_addr < start_addr:
            raise ValueError("无效的地址范围")

        try:
            with open(self.file_path, 'rb') as f:
                # 定位到起始地址
                f.seek(start_addr)
                # 计算要读取的长度
                length = end_addr - start_addr
                # 读取指定范围的数据
                data = f.read(length)

                # 验证是否读取到足够的数据
                if len(data) != length:
                    raise ValueError(f"无法读取完整范围(文件可能太小)，请求长度: {length}，实际读取: {len(data)}")

                return data

        except IOError as e:
            raise IOError(f"文件读取失败: {e}")
