def main():
    v = ["a", "e", "i", "o", "u"]
    x = input().lower()
    i = 0

    for c in x:
        if c in v:
            i += 1

    print(i)


if __name__ == "__main__":
    main()
