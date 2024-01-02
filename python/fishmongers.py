def main():
    _, m = map(int, input().split())
    weights = [int(x) for x in input().split()]
    mongers = []
    for _ in range(m):
        x, y = map(int, input().split())
        mongers.append([x, y])

    weights = sorted(weights)
    mongers = sorted(mongers, key=lambda x: x[1])

    money = 0
    while weights:

        if not mongers:
            break

        fish, price = mongers[-1]

        for _ in range(fish):
            w = weights.pop()
            money += w * price
            if not weights:
                break

        mongers.pop()
    print(money)


if __name__ == "__main__":
    main()
