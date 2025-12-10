def hannoacc(n, a, b, c):
    if n == 1:
        print("{a}-->{c}")

    return hannoacc(n - 1, a, c, b)


hannoacc(3, "A", "B", "C")
