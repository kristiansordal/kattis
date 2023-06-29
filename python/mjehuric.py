def main():
    ints = list(map(int, input().split()))

    while not all(ints[i] <= ints[i + 1] for i in range(len(ints) - 1)):
        for i in range(len(ints) - 1):
            if ints[i] > ints[i + 1]:
                s = ints[i]
                ints[i] = ints[i + 1]
                ints[i + 1] = s
                s = ""
                print(" ".join(map(str, ints)))


if __name__ == "__main__":
    main()
