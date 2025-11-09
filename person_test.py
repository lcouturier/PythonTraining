import unittest

from person import Person, Gender


class MyTestCase(unittest.TestCase):
    def test_person_email(self):
        p1 = Person("Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com")
        self.assertEqual(p1.email, "laurent.couturier@gmail.com")

        p2 = Person("Doe", "Jane", 25, gender=Gender.FEMALE)
        self.assertEqual(p2.email, "jane.doe@example.com")

        p3 = Person("Smith", "Alice", 40, gender=Gender.UNKNOWN)
        self.assertEqual(p3.gender, Gender.UNKNOWN)

        p1 += 10
        self.assertEqual(p1.age, 40)

        p1 -= 5
        self.assertEqual(p1.age, 35)





if __name__ == '__main__':
    unittest.main()
