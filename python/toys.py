def main():
    t, k = map(int, input().split())
    res = 0

    for i in range(2, t + 1):
        res = (res + k) % i
        print(res)

    print(res)


if __name__ == "__main__":
    main()
