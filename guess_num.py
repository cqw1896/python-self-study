import random


def guess_num(random_num):
    count = 0
    while True:
        guess_num_input = input("你猜的数字是: ")
        try:
            guess_num = int(guess_num_input)
        except ValueError:
            print("输入的不是数字")
            continue
        if random_num != guess_num and guess_num < random_num:
            print("你猜小了")
            count += 1
            continue
        elif random_num != guess_num and guess_num > random_num:
            print("大了")
            count += 1
            continue
        print(f"猜对了: {guess_num}")
        count += 1
        print(f"总共猜了 {count} 次")
        s = input("是否继续猜游戏？继续(y),退出(q): ")
        if s.lower() == "y":
            random_num = random.randint(1, 100)
            count = 0
            continue
        break


def main():
    random_num = random.randint(1, 100)
    guess_num(random_num)


if __name__ == "__main__":
    main()
