from lazy import Lazy

import pytest


def test_lazy_evaluates_only_once():
    calls = []

    def factory():
        calls.append("x")
        return 99

    lazy = Lazy(factory)
    assert not lazy.has_value
    assert lazy.is_empty

    first = lazy.value
    second = lazy.value
    assert first == 99
    assert second == 99
    assert calls == ["x"]
    assert lazy.has_value
    assert not lazy.is_empty


def test_lazy_call_and_str():
    lazy = Lazy(lambda: "foo")
    assert lazy() == "foo"
    assert "value: 'foo'" in str(lazy)


def test_lazy_truthiness_toggles_correctly():
    lazy = Lazy(lambda: 1)
    assert not bool(lazy)
    _ = lazy.value
    assert bool(lazy)


def test_lazy_of_static_returns_lazy():
    lazy = Lazy.of(lambda: 42)
    assert isinstance(lazy, Lazy)
    assert lazy.value == 42


def test_lazy_reset_clears_cache():
    calls = []

    def factory():
        calls.append("do")
        return [3, 4]

    lazy = Lazy(factory)
    assert lazy.value == [3, 4]
    assert calls == ["do"]
    lazy.reset()
    assert not lazy.has_value
    assert lazy.value == [3, 4]
    assert calls == ["do", "do"]


def test_lazy_repr_is_correct():
    def f():
        return 123

    lazy = Lazy(f)
    assert repr(lazy) == f"Lazy({f!r})"


def test_lazy_value_assertion():
    lazy = Lazy(lambda: None)
    with pytest.raises(AssertionError):
        # Force an invalid internal state (should not happen in practice)
        lazy._evaluated = True
        lazy._value = None
        _ = lazy.value


def test_lazy_with_complex_types():
    d = {"x": 42, "y": [1, 2]}

    def factory():
        return {k: v[:] if isinstance(v, list) else v for k, v in d.items()}

    lazy = Lazy(factory)
    val = lazy.value
    assert val == d
    # Changing original should not affect value (shallow copy test)
    d["y"].append(3)
    assert val["y"] == [1, 2]


@pytest.mark.parametrize(
    "func,result",
    [
        (lambda: 7, 7),
        (lambda: "abc", "abc"),
        (lambda: [0, 1], [0, 1]),
    ],
)
def test_lazy_parametrized(func, result):
    lazy = Lazy(func)
    assert lazy.value == result
    assert lazy.has_value
    assert not lazy.is_empty
