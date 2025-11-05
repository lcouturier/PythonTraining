import copy

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
            case 'male':
                return Gender.MALE
            case 'female':
                return Gender.FEMALE
            case 'other':
                return Gender.OTHER
            case _:
                raise ValueError(f"Unknown gender: {label}")

    @staticmethod
    def from_ordinal():
        items = {
            0: Gender.UNKNOWN,
            1: Gender.MALE,
            2: Gender.FEMALE,
            3: Gender.OTHER
        }

        def inner(i):
            return items.get(i, Gender.UNKNOWN)

        return inner


class Person:
    def __init__(self, last_name, first_name, age, gender=Gender.MALE, email=None):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.email = email is not None and email or ""

    def __repr__(self):
        return f"Person(last_name='{self.last_name}', first_name='{self.first_name}', age={self.age})"

    def __eq__(self, other):
        return (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.age == other.age)

    def __bool__(self):
        return self.age > 0

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "age": self.age,
        }

    def to_tuple(self):
        return self.last_name, self.first_name, self.age

    def to_string(self):
        return f"{self.last_name}, {self.first_name}, {self.age}"

    def is_adult(self):
        return self.age >= 18

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"

    @property
    def is_senior(self):
        return self.age >= 65

    @property
    def gender_str(self):
        return self.gender.value

    @property
    def typology(self):
        match self.age:
            case age if age < 12:
                return "Child"
            case age if 12 <= age < 20:
                return "Teenager"
            case age if 20 <= age < 65:
                return "Adult"
            case _:
                return "Senior"

    @property
    def greet(self):
        return f"Hello, my name is {self.full_name()} and I am {self.age} years old."

    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.first_name}! You are now {self.age} years old."

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    g = Gender.MALE
    print(g)
    print(g.value)
    print(Gender.from_str("Female"))

    f = Gender.from_ordinal()
    print(f(1))
    print(f(2))
    print(f(99))
