import unittest

from person import Person, Gender


class PersonTestCase(unittest.TestCase):
    def test_person_email(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1.email, "laurent.couturier@gmail.com")

        p2 = Person("Doe", "Jane", 25, gender=Gender.FEMALE)
        self.assertEqual(p2.email, "jane.doe@example.com")

        p3 = Person("Smith", "Alice", 40, gender=Gender.UNKNOWN)
        self.assertEqual(p3.gender, Gender.UNKNOWN)

        p1 += 10
        self.assertEqual(p1.age, 40)

        p1 -= 5
        self.assertEqual(p1.age, 35)

    def test_person_age_negative(self):
        with self.assertRaises(ValueError):
            Person("Doe", "John", -5, gender=Gender.MALE)

    def test_person_clone(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        p2 = p1.clone()
        self.assertEqual(p1, p2)

    def test_person_str(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(str(p1), "Doe, John (30 years old)")

    def test_person_eq(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        p2 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1, p2)

    def test_person_lt(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        p2 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1, p2)

    def test_person_gt(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        p2 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1, p2)

    def test_person_hash(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        p2 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(hash(p1), hash(p2))

    def test_person_is_adult(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1.is_adult, True)

    def test_person_is_senior(self):
        p1 = Person(
            "Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com"
        )
        self.assertEqual(p1.is_senior, False)


if __name__ == "__main__":
    unittest.main()
