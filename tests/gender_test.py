import unittest

from gender import Gender


class TestGenderEnum(unittest.TestCase):
    def test_enum_members_and_values(self):
        self.assertEqual(Gender.FEMALE.value, "Féminin")
        self.assertEqual(Gender.MALE.value, "Masculin")
        self.assertEqual(Gender.NON_BINARY.value, "Non-Binaire")
        self.assertEqual(Gender.OTHER.value, "Autre")
        self.assertEqual(Gender.PREFER_NOT_SAY.value, "Préfère ne pas dire")

    def test_str_returns_value(self):
        for gender in Gender:
            self.assertEqual(str(gender), gender.value)

    def test_repr_returns_expected_format(self):
        for gender in Gender:
            self.assertEqual(repr(gender), f"Gender.{gender.name}")

    def test_bool_true_for_non_other(self):
        self.assertTrue(bool(Gender.FEMALE))
        self.assertTrue(bool(Gender.MALE))
        self.assertTrue(bool(Gender.NON_BINARY))
        self.assertTrue(bool(Gender.PREFER_NOT_SAY))

    def test_bool_false_for_other(self):
        self.assertFalse(bool(Gender.OTHER))

    def test_from_str_valid_inputs(self):
        test_cases = [
            ("female", Gender.FEMALE),
            ("Féminin", Gender.FEMALE),
            ("male", Gender.MALE),
            ("masculin", Gender.MALE),
            ("non-binary", Gender.NON_BINARY),
            ("Non-Binaire", Gender.NON_BINARY),
            ("other", Gender.OTHER),
            ("autre", Gender.OTHER),
            ("prefer not say", Gender.PREFER_NOT_SAY),
            ("Préfère ne pas dire", Gender.PREFER_NOT_SAY),
            ("  Féminin   ", Gender.FEMALE),
            ("MaLe", Gender.MALE),
        ]
        for label, expected in test_cases:
            with self.subTest(label=label):
                self.assertEqual(Gender.from_str(label), expected)

    def test_from_str_invalid_input_raises(self):
        invalid_labels = ["unknown", "", "xyz", "man", None]
        for label in invalid_labels:
            with self.subTest(label=label):
                if label is None:
                    with self.assertRaises(AttributeError):
                        Gender.from_str(label)
                else:
                    with self.assertRaises(ValueError):
                        Gender.from_str(label)

    def test_from_ordinal_valid_indices(self):
        for i, expected in enumerate(list(Gender)):
            with self.subTest(ordinal=i):
                self.assertEqual(Gender.from_ordinal(i), expected)

    def test_from_ordinal_invalid_index_returns_other(self):
        self.assertEqual(Gender.from_ordinal(-1), Gender.OTHER)
        self.assertEqual(Gender.from_ordinal(100), Gender.OTHER)

    def test_from_ordinal_type_error_returns_other(self):
        for invalid in ["a", None, 3.7]:
            with self.subTest(val=invalid):
                self.assertEqual(Gender.from_ordinal(invalid), Gender.OTHER)

    def test_enum_is_iterable_and_complete(self):
        expected_members = [
            Gender.FEMALE,
            Gender.MALE,
            Gender.NON_BINARY,
            Gender.OTHER,
            Gender.PREFER_NOT_SAY,
        ]
        self.assertListEqual(list(Gender), expected_members)


if __name__ == "__main__":
    unittest.main()
