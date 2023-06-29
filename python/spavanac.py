def main():
    h, m = map(int, input().split())

    if m < 45:
        m = 60 + m - 45
        h -= 1
        if h < 0:
            h = 23
    else:
        m -= 45

    print(h, " ", m)


if __name__ == "__main__":
    main()
