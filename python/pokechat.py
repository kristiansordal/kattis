def main():
    s = input()
    c = input()
    ids = [int(char) for id, char in enumerate(c, start=1) if id % 3 == 0]
    code = []

    for i in ids:
        code.append(s[i - 1])
    print("".join(code))


if __name__ == "__main__":
    main()
