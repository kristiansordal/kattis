def knapsack(p, X):
    n = len(p)
    dp = [[0 for _ in range(X + 1)] for _ in range(n + 1)]
    vals = [[0 for _ in range(X + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if dp[i - 1][j] + p[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + p[i - 1]
                vals[i][j] = vals[i - 1][j] + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
                vals[i][j] = max(vals[i - 1][j - 1], vals[i - 1][j])

    for r in dp:
        print(" ".join(map(str, r)))

    print(vals[-1][-1])


def main():
    _, X = map(int, input().split())
    prices = [int(x) for x in input().split()]
    print(prices)
    print(knapsack(prices, X))


if __name__ == "__main__":
    main()
    # print(knapsack(list(range(0, 6)), prices, X))
