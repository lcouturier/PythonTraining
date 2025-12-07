from dataclasses import dataclass
import enum
from typing import Any, Optional
from gender import Gender


class Typology(enum.Enum):
    """Enumeration for a person's age-based typology."""

    CHILD = "Child"
    TEENAGER = "Teenager"
    ADULT = "Adult"
    SENIOR = "Senior"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_ordinal(cls, ordinal: int) -> "Typology":
        """Return Typology member by its ordinal (declaration order).

        Args:
            ordinal (int): Index of the enum member (0-based).

        Returns:
            Typology: Corresponding Typology enum value.

        Raises:
            IndexError: If ordinal is out of range.
        """
        members = list(cls)
        if 0 <= ordinal < len(members):
            return members[ordinal]
        raise IndexError(f"Ordinal {ordinal} is out of range for Typology enum.")


@dataclass(frozen=True, order=True)
class Person:
    """Represents an immutable person with basic demographic information.

    Attributes:
        last_name (str): The person's last name.
        first_name (str): The person's first name.
        age (int): The person's age in years.
        gender (Gender, optional): The person's gender. Defaults to Gender.OTHER.
        email (Optional[str], optional): The person's email address. Defaults to None.
    """

    last_name: str
    first_name: str
    age: int
    gender: Gender = Gender.OTHER
    email: Optional[str] = None

    def full_name(self) -> str:
        """Returns the person's full name in 'First Last' format.

        Returns:
            str: Full name in 'First Last' format.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        """Determines if the person is an adult (18 years or older).

        Returns:
            bool: True if age >= 18, else False.
        """
        return self.age >= 18

    @property
    def is_senior(self) -> bool:
        """Determines if the person is a senior (65 years or older).

        Returns:
            bool: True if age >= 65, else False.
        """
        return self.age >= 65

    def __str__(self) -> str:
        """Returns a readable string representation of the person.

        Returns:
            str: Human-readable description.
        """
        return f"{self.last_name}, {self.first_name} ({self.age} years old)"

    def __repr__(self) -> str:
        """Returns the official string representation of the Person.

        Returns:
            str: Representation containing all attributes.
        """
        return (
            f"Person("
            f"last_name={self.last_name!r}, "
            f"first_name={self.first_name!r}, "
            f"age={self.age!r}, "
            f"gender={self.gender!r}, "
            f"email={self.email!r})"
        )

    @property
    def typology(self) -> Typology:
        """Provides the typological category for the person based on age.

        Returns:
            Typology: One of Typology.CHILD, Typology.TEENAGER, Typology.ADULT, or Typology.SENIOR.
        """
        if self.age < 12:
            return Typology.CHILD
        if self.age < 20:
            return Typology.TEENAGER
        if self.age < 65:
            return Typology.ADULT
        return Typology.SENIOR

    def to_dict(self) -> dict[str, Any]:
        """Converts the Person instance to a dictionary.

        Returns:
            dict[str, Any]: A dictionary representation of the person.
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "age": self.age,
            "gender": self.gender.name,
            "email": self.email,
        }


def _demo_person_usage() -> None:
    """Demonstrates usage of the Person class."""
    p1 = Person(
        last_name="Doe",
        first_name="John",
        age=30,
        gender=Gender.MALE,
        email="laurent.couturier@gmail.com",
    )
    p2 = Person(last_name="Doe", first_name="Jane", age=25, gender=Gender.FEMALE)
    print(p1)
    print(p1.gender.value)
    print(p2)
    print(p1 == p2)
    print(p1.is_adult)
    print(p2.is_senior)


if __name__ == "__main__":
    _demo_person_usage()
