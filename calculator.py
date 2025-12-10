#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def calcuator():
    """主计算器函数"""
    print("=" * 40)
    print("欢迎使用简易计算器")
    print("=" * 40)

    while True:
        # 显示菜单
        print("\n请选择运算类型: ")
        print("1. 加法（+）")
        print("2. 减法（-）")
        print("3. 乘法（*）")
        print("4. 除法（/）")
        print("5. 幂运算（**）")
        print("6. 取余（%）")
        print("7. 整除（//）")
        print("8. 开方（√）")
        print("9. 退出")
        print("-" * 40)

        # 获取用户选择
        choice = input("请输入选项: (1-9): ")

        # 退出条件
        if choice == "9":
            print("\n感谢使用计算器，再见！")
            break

        # 检查输入是否有效
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("\n错误：无效选项，请重新选择！")
            continue

        # 获取数字（开方只需要一个数字）
        try:
            num1 = float(input("\n请输入第一个数字："))
            # 开方运算只需要一个数字
            if choice == "8":
                num2 = None
            else:
                num2 = float(input("请输入第二个数字："))
        except ValueError:
            print("\n错误：请输入有效数字！")
            continue
        # 根据选择执行计算
        if choice == "1":
            result = num1 + num2
            operator = "+"
        elif choice == "2":
            result = num1 - num2
            operator = "-"
        elif choice == "3":
            result = num1 * num2
            poerator = "*"
        elif choice == "4":
            # 检查除数是否为0
            if num2 == 0:
                print("\n错误：除数不能为零！")
                continue
            result = num1 / num2
            operator = "/"
        elif choice == "5":
            result = num1**num2
            operator = "**"
        elif choice == "6":
            if num2 == 0:
                print("\n错误：除数不能为零！")
                continue
            result = num1 % num2
            operator = "%"
        elif choice == "7":
            if num2 == 0:
                print("\n错误：除数不能为零！")
                continue
            result = num1 // num2
            operator = "//"
        elif choice == "8":
            # 检查是否为负数
            if num1 < 0:
                print("\n错误：不能对负数开方！")
                continue
            result = num1**0.5
            operator = "√"
        # 显示结果
        if choice == "8":
            print(f"\n结果：√{num1} = {result}")
        else:
            print(f"\n结果：{num1} {operator} {num2} = {result}")
        print("=" * 40)


if __name__ == "__main__":
    calcuator()
