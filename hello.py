def hello(name: str = "world") -> str:
    """返回问候语"""
    return f"Hello, {name}"


if __name__ == "__main__":
    print(hello())
