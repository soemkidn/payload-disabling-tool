import unittest

import core

input_file = './test_files/payload.exe'

output_file = './test_files/blocked_payload.exe'

class MyTestCase(unittest.TestCase):
    def testParsing(self):
        print("testParsing")
        parser = core.PEParser(input_file)
        parser.extract_config()
        self.assertNotEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
