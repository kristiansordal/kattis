def flip(x):
    return (x[1], x[0])


def getList(x):
    return list(map(lambda x: x[1] + 2, x))


def main():
    _ = int(input())
    p = []

    xs = map(int, input().split())
    for x in xs:
        p.append(x)

    p = enumerate(p)
    p = getList(sorted(list(map(lambda x: flip(x), p))))

    print("1 ", " ".join(list(map(str, p))))


if __name__ == "__main__":
    main()
