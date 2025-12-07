from enum import Enum


class Gender(Enum):
    FEMALE = "Féminin"
    MALE = "Masculin"
    NON_BINARY = "Non-Binaire"
    OTHER = "Autre"
    PREFER_NOT_SAY = "Préfère ne pas dire"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    def __bool__(self) -> bool:
        return self is not Gender.OTHER

    @staticmethod
    def from_str(label: str) -> "Gender":
        normalized = label.strip().lower()
        mapping = {
            "female": Gender.FEMALE,
            "féminin": Gender.FEMALE,
            "male": Gender.MALE,
            "masculin": Gender.MALE,
            "non-binary": Gender.NON_BINARY,
            "non binaire": Gender.NON_BINARY,
            "non-binaire": Gender.NON_BINARY,
            "other": Gender.OTHER,
            "autre": Gender.OTHER,
            "prefer not say": Gender.PREFER_NOT_SAY,
            "préfère ne pas dire": Gender.PREFER_NOT_SAY,
        }
        try:
            return mapping[normalized]
        except KeyError as exc:
            raise ValueError(f"Unknown gender: {label}") from exc

    @classmethod
    def from_ordinal(cls, ordinal: int) -> "Gender":
        if not isinstance(ordinal, int):
            return cls.OTHER
        # Enum iteration order guaranteed in Python 3.11+
        members = list(cls)
        if 0 <= ordinal < len(members):
            return members[ordinal]
        return cls.OTHER
