from person import Typology

import pytest


@pytest.mark.parametrize(
    "ordinal, expected",
    [
        (0, Typology.CHILD),
        (1, Typology.TEENAGER),
        (2, Typology.ADULT),
        (3, Typology.SENIOR),
    ],
)
def test_typology_from_ordinal_valid(ordinal, expected):
    assert Typology.from_ordinal(ordinal) == expected


@pytest.mark.parametrize("ordinal", [-1, 4, 100])
def test_typology_from_ordinal_invalid(ordinal):
    with pytest.raises(IndexError):
        Typology.from_ordinal(ordinal)


@pytest.mark.parametrize(
    "member, string",
    [
        (Typology.CHILD, "Child"),
        (Typology.TEENAGER, "Teenager"),
        (Typology.ADULT, "Adult"),
        (Typology.SENIOR, "Senior"),
    ],
)
def test_typology_str(member, string):
    assert str(member) == string


def test_typology_enum_membership():
    members = list(Typology)
    assert members == [
        Typology.CHILD,
        Typology.TEENAGER,
        Typology.ADULT,
        Typology.SENIOR,
    ]
