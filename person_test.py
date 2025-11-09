import unittest

from person import Person, Gender


class MyTestCase(unittest.TestCase):
    def test_person_email(self):
        p1 = Person("Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com")
        self.assertEqual(p1.email, "laurent.couturier@gmail.com")

        p2 = Person("Doe", "Jane", 25, gender=Gender.FEMALE)
        self.assertEqual(p2.email, "jane.doe@example.com")


if __name__ == '__main__':
    unittest.main()
