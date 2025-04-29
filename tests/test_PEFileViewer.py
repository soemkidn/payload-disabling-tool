import unittest
from core.PEFileViewer import PEFileViewer
from core.PEParser import PEParser

input_file = './test_files/payload.exe'

output_file = './test_files/blocked_payload.exe'

class MyTestCase(unittest.TestCase):
    def testFileViewer(self):
        parser = PEParser(input_file)
        parser.extract_config()
        viewer = PEFileViewer(input_file)
        ip = viewer.view_hex_range(parser.ips[0].start, parser.ips[0].end)
        port = viewer.view_hex_range(parser.ports[0].start, parser.ports[0].end)
        self.assertEqual(ip, b"\xAC\x1B\x2C\xBA")
        self.assertEqual(port, b"\x11\x5C")


if __name__ == '__main__':
    unittest.main()
