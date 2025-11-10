import unittest

from gender import Gender


class MyTestCase(unittest.TestCase):
    def test_from_ordinal(self):
        get_gender = Gender.from_ordinal()
        gender = get_gender(1)  # Returns Gender.MALE
        self.assertEqual(gender, Gender.MALE)  # add assertion here

        gender = get_gender(99)  # Returns Gender.MALE
        self.assertEqual(gender, Gender.UNKNOWN)  # add assertion here

    def test_from_str(self):
        gender = Gender.from_str("male")
        self.assertEqual(gender, Gender.MALE)

        gender = Gender.from_str("female")
        self.assertEqual(gender, Gender.FEMALE)

        gender = Gender.from_str("other")
        self.assertEqual(gender, Gender.OTHER)

    def test_from_str_exception(self):
        with self.assertRaises(ValueError):
            Gender.from_str("unknown")




if __name__ == '__main__':
    unittest.main()
