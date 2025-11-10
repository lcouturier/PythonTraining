from enum import Enum


class Gender(Enum):
    UNKNOWN = "Unknown"
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(label):
        match label.lower():
            case "male":
                return Gender.MALE
            case "female":
                return Gender.FEMALE
            case "other":
                return Gender.OTHER
            case _:
                raise ValueError(f"Unknown gender: {label}")

    @staticmethod
    def from_ordinal():
        """
        Returns a function that maps an ordinal to a Gender.

        :return: A function that maps an ordinal to a Gender.
        :rtype: Callable[[int], Gender]
        """
        gender_map = {0: Gender.UNKNOWN, 1: Gender.MALE, 2: Gender.FEMALE, 3: Gender.OTHER}

        def map_ordinal_to_gender(ordinal):
            """
            Maps an ordinal to a Gender.

            :param ordinal: The ordinal to map.
            :type ordinal: int
            :return: The corresponding Gender.
            :rtype: Gender
            """
            return gender_map.get(ordinal, Gender.UNKNOWN)

        return map_ordinal_to_gender
