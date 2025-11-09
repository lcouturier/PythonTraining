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
    def __init__(self, last_name: str, first_name: str, age: int, gender: Gender | None, email: str = None):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender is not None and gender or Gender.UNKNOWN
        self.email = email is not None and email or f"{first_name.lower()}.{last_name.lower()}@example.com"

    def __repr__(self):
        return f"Person(last_name='{self.last_name}', first_name='{self.first_name}', age={self.age})"

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.age} years old)"

    def __eq__(self, other):
        return (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.age == other.age)

    def __bool__(self):
        return self.age > 0

    def __iadd__(self, other):
        if isinstance(other, int):
            self.age += other
            return self
        raise TypeError("Operand must be an integer")

    def __isub__(self, other):
        if isinstance(other, int):
            self.age -= other
            return self
        raise TypeError("Operand must be an integer")



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
    p1 = Person("Doe", "John", 30, gender=Gender.MALE, email="laurent.couturier@gmail.com")
    p2 = Person("Doe", "Jane", 25, gender=Gender.FEMALE)
    print(p1)
    print(p2)
    print(p1 == p2)
    print(p1.is_adult())
    print(p2.is_senior)
    print(p1.greet)
    print(p2.birthday())
    p3 = p1.clone()
    print(p3)
    print(p1 == p3)
    print(str(p1))
    print(str(p2))
    print(p1.email)
