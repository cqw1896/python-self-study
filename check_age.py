def is_adult(age: int) -> str:
    return "成年人" if age >= 18 else "未成年"


def main():
    while True:
        age_input = input("请输入你的年龄(或输入 q 退出): ")
        if age_input.lower() == "q":
            print("已退出")
            break
        try:
            age = int(age_input)
        except ValueError:
            print("请输入有效数字！")
            continue
        print(is_adult(age))


if __name__ == "__main__":
    main()
