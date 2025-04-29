import unittest

from core.PEParser import PEParser

input_file = './test_files/payload.exe'

output_file = './test_files/blocked_payload.exe'

class MyTestCase(unittest.TestCase):
    def testParsing(self):
        print("testParsing")
        parser = PEParser(input_file)
        parser.extract_config()
        for ip in parser.ips:
            print(ip.toString())
            self.assertNotEqual(ip.start, 17749)
            self.assertNotEqual(ip.end, 17753)
        for port in parser.ports:
            print(port.toString())
            self.assertNotEqual(port.start, 17756)
            self.assertNotEqual(port.end, 17758)



if __name__ == '__main__':
    unittest.main()
