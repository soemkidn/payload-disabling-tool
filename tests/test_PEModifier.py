import unittest
from core.PEModifier import PEModifier
from core.PEParser import PEParser
from core.PEFileViewer import PEFileViewer

input_file = './test_files/payload.exe'

output_file = './test_files/blocked_payload.exe'

class MyTestCase(unittest.TestCase):
    def testModification(self):
        parser = PEParser(input_file)
        viewer = PEFileViewer(output_file)
        parser.extract_config()
        modifier = PEModifier(input_file, output_file)
        modifier.modify_pe_hex_string(parser.ips[0].start, parser.ips[0].end, b'\x7F\x00\x00\x01')
        modifier = PEModifier(output_file, output_file)
        modifier.modify_pe_hex_string(parser.ports[0].start, parser.ports[0].end, b'\x00\x50')
        new_ip = viewer.view_hex_range(parser.ips[0].start, parser.ips[0].end)
        new_port = viewer.view_hex_range(parser.ports[0].start, parser.ports[0].end)
        self.assertEqual(new_ip, b'\x7F\x00\x00\x01')
        self.assertEqual(new_port, b'\x00\x50')


if __name__ == '__main__':
    unittest.main()
