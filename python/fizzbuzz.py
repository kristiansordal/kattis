def main():
    x, y, n = map(int, input().split())

    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
            continue
        if i % x == 0:
            print("Fizz")
            continue
        if i % y == 0:
            print("Buzz")
            continue
        else:
            print(i)


if __name__ == "__main__":
    main()
