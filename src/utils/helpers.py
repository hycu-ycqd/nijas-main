"""QA utility helpers."""


def greet(name: str) -> str:
    message = f"Hello, {name}!"
    print(message)
    return message


def add(a: int, b: int) -> int:
    return a + b


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")
