import random


def guess_number_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("我已经想好了一个 1-100 之间的数字，快来猜吧！")

    while True:
        user_input = input("请输入你的猜测（或输入 q 退出）").strip()
        attempts += 1
        if user_input.lower() == "q":
            print("已退出，游戏结束。")
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("输入无效，请输入整数或 q。")
            attempts -= 1  # 本次不算有效尝试
            continue

        if guess < secret:
            print("太小了，再试试！")
        elif guess > secret:
            print("太大了，再试试！")
        else:
            print(f"恭喜！你用了 {attempts} 次猜中数字 {secret}！")
            break


if __name__ == "__main__":
    guess_number_game()
