def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        print(x, sum(range(2, y + 2)))


if __name__ == "__main__":
    main()
