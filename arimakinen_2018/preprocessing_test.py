import unittest

import preprocessing


class TestSweet(unittest.TestCase):
    def strings_to_sec_test(self):
        time_string = '2:34.8'
        result = preprocessing.strings_to_sec(time_string)
        self.assertEqual(result, float(154.8))


if __name__ == '__main__':
    unittest.main()
