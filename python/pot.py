import sys


def main():
    nums = [((x.strip())[:-1], x.strip()[-1]) for x in sys.stdin.readlines()]

    s = 0
    for n in nums:
        # print(n)
        if not n[0] == "":
            # s += int(n[1]) ** 0
            # else:
            s += int(n[0]) ** int(n[1])

    print(s)


if __name__ == "__main__":
    main()
