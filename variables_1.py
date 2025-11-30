def variables(name: str, age: int) -> str:
    return f"Hello, {name}, you are {age} years old."


def main():
    """入口函数，处理 I/O (副作用)"""
    name = input("请输入你的姓名: ")
    age_input = input("请输入你的年龄: ")
    try:
        age = int(age_input)
    except ValueError:
        print("年龄必须是数字!")
        return
    print(variables(name, age))


if __name__ == "__main__":
    main()
