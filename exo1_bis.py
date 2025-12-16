from functools import reduce
from mimetypes import init
from typing import Iterator, Tuple
import requests as request
import browser_cookie3


def get_session_cookie(*, domain_name: str) -> str:
    cookies = browser_cookie3.chrome(domain_name=domain_name)
    session = next(
        (cookie.value for cookie in cookies if cookie.name == "session"), None
    )

    if session is not None:
        return session
    raise ValueError(
        f"Cookie 'session' introuvable. Es-tu connecté au domaine {domain_name} ?"
    )


def load_from_web(url: str) -> Iterator[str]:
    session_cookie = get_session_cookie(domain_name="adventofcode.com")
    cookies = {"session": session_cookie}
    headers = {"User-Agent": "python-requests"}
    with request.get(url, cookies=cookies, headers=headers) as response:
        if response.status_code != 200:
            raise ValueError(f"Invalid response code: {response.status_code}")
        yield from (line.strip() for line in response.text.split("\n") if line.strip())


def acc(acc: Tuple[int, int], item: str) -> Tuple[int, int]:
    start_val, count = acc
    delta = -int(item[1:]) if item[0] == "L" else int(item[1:])
    new_start = (start_val + delta) % 100
    count += new_start == 0
    return new_start, count


def main():
    filtered_items = [
        item
        for item in list(load_from_web("https://adventofcode.com/2025/day/1/input"))
        if item[0] in ["L", "R"] and item[1:].isnumeric()
    ]
    initial_value = (50, 0)
    _, count = reduce(acc, filtered_items, initial_value)
    print(count)


if __name__ == "__main__":
    main()
