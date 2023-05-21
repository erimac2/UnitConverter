import sys  
sys.path.append("./")

import unittest
from src.converter import convertLength

class TestConverter(unittest.TestCase):
    def test_convert_Length(self):
        self.assertEqual(convertLength(12, 'm', 'A'), 1.2e+11)

unittest.main()