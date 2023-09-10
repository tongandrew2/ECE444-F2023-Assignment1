import unittest
from utils import utils
class Testing(unittest.TestCase):
    def test_reversed(self):
        testutils = utils()
        self.assertEqual(testutils.reversed(54102), 20145)
        self.assertEqual(testutils.reversed(54102.22), "Incorrect input; not an integer")
        self.assertEqual(testutils.reversed("string"), "Incorrect input; not an integer")

    def test_formatter(self):
        testutils = utils()
        self.assertEqual(testutils.formatter(100), ('0b1100100', '0o144'))
        self.assertEqual(testutils.reversed(54102.22), "Incorrect input; not an integer")
        self.assertEqual(testutils.reversed("string"), "Incorrect input; not an integer")

if __name__ == '__main__':
    unittest.main()



