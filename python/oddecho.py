def main():
    n = int(input())
    x = [input() for _ in range(0, n)]

    for i in range(0, n):
        if i % 2 == 0:
            print(x[i])


if __name__ == "__main__":
    main()
