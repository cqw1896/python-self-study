def main():
    print("遍历 1-100，统计偶数个数")
    even_cnt = 0
    for i in range(1, 101):
        if i % 2 == 0:
            even_cnt += 1
    print(f"偶数个数 = {even_cnt}")
    # while 示例：读取用户输入直到输入 q
    print("\n输入任意数字，输入 q 结束: ")
    while True:
        s = input("> ")
        if s.lower() == "q":
            print("已退出")
            break
        try:
            num = float(s)
            print(f"你输入的数字是 {num}")
        except ValueError:
            print("请输入数字或 q! ")
            continue


if __name__ == "__main__":
    main()
