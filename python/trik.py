def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def main():
    a, b, c = 1, 0, 0
    y = input()

    for i in y:
        if i == "A":
            a, b = swap(a, b)
        elif i == "B":
            b, c = swap(b, c)
        elif i == "C":
            a, c = swap(a, c)

    if a == 1:
        print(1)
    elif b == 1:
        print(2)
    elif c == 1:
        print(3)


if __name__ == "__main__":
    main()
