from math import floor, log


def main():
    n, k = map(int, input().split())
    # if n < k**2:
    #     print(floor(n / k + 1))
    # else:
    p = log((n * (k - 1) + 1), k)
    ones = ((k ** (p)) - 1) / (k - 1)
    i = 1
    while ones >= n:
        ones = ((k ** (p - i)) - 1) / (k - 1)

    print(floor(ones))


if __name__ == "__main__":
    main()
