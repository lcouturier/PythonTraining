from enum import Enum

from annotations import memoize


class Gender(Enum):
    UNKNOWN = "Unknown"
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    def __str__(self):
        return self.value

    @staticmethod
    @memoize
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
        items = {0: Gender.UNKNOWN, 1: Gender.MALE, 2: Gender.FEMALE, 3: Gender.OTHER}

        def inner(i):
            return items.get(i, Gender.UNKNOWN)

        return inner
