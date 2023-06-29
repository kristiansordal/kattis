def main():
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        print("Not a moose")

    elif x == y:
        print(f"Even {x + y}")
    else:
        m = max(x, y)
        print(f"Odd {m + m}")


if __name__ == "__main__":
    main()
