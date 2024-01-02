import sys
import random


# def knapsack(v, w, W):
#     n = len(v)
#     dp = [[0 for _ in range(W + 1)] for _ in range(n)]
#     ids = [[False for _ in range(W + 1)] for _ in range(n)]

#     for i in range(n):
#         for j in range(W + 1):
#             if w[i] > j:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 if dp[i - 1][j] > dp[i - 1][j - w[i]] + v[i]:
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     dp[i][j] = dp[i - 1][j - w[i]] + v[i]
#                     ids[i][j] = True

#     i, j = n - 1, W
#     seq = []

#     while i >= 0 and j >= 0:
#         if ids[i][j]:
#             seq.append(i)
#             j -= w[i]
#         i -= 1

#     seq.reverse()
#     return len(seq), seq


def generate_random_knapsack_instance(num_items, max_value, max_weight, capacity):
    values = [random.randint(1, max_value) for _ in range(num_items)]
    weights = [random.randint(1, max_weight) for _ in range(num_items)]

    return f"{num_items} {capacity}\n" + "\n".join([f"{v} {w}" for v, w in zip(values, weights)])


def knapsack(v, w, W):
    n = len(v)
    dp = [0 for _ in range(W + 1)]
    ids = [[False for _ in range(W + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(W, w[i] - 1, -1):
            if dp[j - w[i]] + v[i] > dp[j]:
                dp[j] = dp[j - w[i]] + v[i]
                ids[i][j] = True

    i, j = n - 1, W
    seq = []

    while i >= 0 and j >= 0:
        if ids[i][j]:
            seq.append(i)
            j -= w[i]
        i -= 1

    seq.reverse()
    return len(seq), seq


def main():
    # inp = sys.stdin.read().split("\n")
    for _ in range(30):
        inp = generate_random_knapsack_instance(2000, 10000, 10000, 2000).split("\n")
        l = len(inp)
        x = 0

        c, n = map(int, inp[0].split())
        x += 1

        while True:
            values = []
            weights = []
            for i in range(x, l):
                v, w = map(int, inp[i].split())
                values.append(v)
                weights.append(w)

            x += n

            n, s = knapsack(values, weights, c)
            print(n)
            print(" ".join(map(str, s)))

            if x >= l - 1:
                break

            c, n = map(int, inp[x].split())
            x += 1


if __name__ == "__main__":
    main()
