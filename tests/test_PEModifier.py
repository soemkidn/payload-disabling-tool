import unittest
from core.PEModifier import PEModifier
from core.PEParser import PEParser

input_file = './test_files/payload.exe'

output_file = './test_files/blocked_payload.exe'

class MyTestCase(unittest.TestCase):
    def testModification(self):
        modifier = PEModifier(input_file, output_file)
        parser = PEParser(input_file)
        parser.extract_config()
        modifier.modify_pe_hex_string(parser.ips[0].start, parser.ips[0].end, b'\\x7F\\x00\\x00\\x01')
        modifier.modify_pe_hex_string(parser.ports[0].start, parser.ports[0].end, b'\\x00\\x50')
        
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
