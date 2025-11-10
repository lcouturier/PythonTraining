import unittest

from gender import Gender


class MyTestCase(unittest.TestCase):
    def test_from_ordinal(self):
        get_gender = Gender.from_ordinal()
        gender = get_gender(1)  # Returns Gender.MALE
        self.assertEqual(gender, Gender.MALE)  # add assertion here

        gender = get_gender(99)  # Returns Gender.MALE
        self.assertEqual(gender, Gender.UNKNOWN)  # add assertion here


if __name__ == '__main__':
    unittest.main()
