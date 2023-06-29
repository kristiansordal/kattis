def main():
    _ = int(input())
    expenses = map(int, (input().split()))
    expenses = sum(list(filter(lambda x: x < 0, expenses)))
    print(abs(expenses))


if __name__ == "__main__":
    main()
