def main():
    name = input("请输入你的姓名: ")
    age_input = input("请输入你的年龄: ")
    try:
        age = int(age_input)
    except ValueError:
        print("年龄必须是数字!")
        return
    print(f"Hello, {name}, you are {age} years old.")


if __name__ == "__main__":
    main()
