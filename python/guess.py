def main():
    lo = 0
    hi = 1000
    mid = hi - (hi - lo) / 2

    print(mid)

    response = input()

    while response != "correct":
        mid = hi - (hi - lo) / 2
        if response == "lower":
            hi = mid - 1

        elif response == "higher":
            lo = mid + 1

        print(mid)
        response = input()


if __name__ == "__main__":
    main()
