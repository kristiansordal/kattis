def main():
    n = int(input())

    prices = []
    for _ in range(n):
        _, price = input().split()
        price = int(price)
        prices.append(price)
    prices = list(reversed(sorted(prices)))

    pay = 0
    for i, p in enumerate(prices):
        if i % 2 == 0:
            pay += p

    print(pay)


if __name__ == "__main__":
    main()
