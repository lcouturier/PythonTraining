import unittest

from result import Failure, Result, Success

import pytest


def test_success_is_success_and_not_failure():
    s = Success(123)
    assert s.is_success()
    assert not s.is_failure()
    assert s.value == 123
    assert s.error is None
    assert repr(s) == "Success(123)"


def test_failure_is_failure_and_not_success():
    f = Failure("err")
    assert not f.is_success()
    assert f.is_failure()
    assert getattr(f, "value", None) is None
    assert f._error == "err"
    assert (
        getattr(f, "error", None) == "err"
    )  # Will fail; error property not defined, but ._error is


def test_result_of_returns_success_when_error_is_none():
    r = Result.of(42)
    assert isinstance(r, Success)
    assert r.value == 42
    assert r.error is None


def test_result_of_returns_failure_when_error_is_not_none():
    r = Result.of(99, error="foo")
    assert isinstance(r, Failure)
    assert r._error == "foo"


def test_when_calls_on_success():
    result = Success("ok")
    called = {"ok": False, "fail": False}

    def on_success(val):
        called["ok"] = True
        assert val == "ok"

    def on_failure(_):
        called["fail"] = True

    result.when(on_success, on_failure)
    assert called["ok"]
    assert not called["fail"]


def test_when_calls_on_failure():
    result = Failure("bad")
    called = {"ok": False, "fail": False}

    def on_success(_):
        called["ok"] = True

    def on_failure(err):
        called["fail"] = True
        assert err == "bad"

    result.when(on_success, on_failure)
    assert not called["ok"]
    assert called["fail"]


def test_map_on_success_transforms_value():
    s = Success(10)
    mapped = s.map(lambda x: x + 5)
    assert isinstance(mapped, Success)
    assert mapped.value == 15


def test_map_on_failure_passes_failure():
    f = Failure("fail")
    mapped = f.map(lambda x: x + 5)
    assert isinstance(mapped, Failure)
    assert getattr(mapped, "_error") == "fail"


@pytest.mark.parametrize(
    "res,expected",
    [
        (Success("hi"), True),
        (Failure("oops"), False),
    ],
)
def test_is_success_and_is_failure(res, expected):
    assert res.is_success() is expected
    assert res.is_failure() is not expected
