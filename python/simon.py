def main():
    n = int(input())
    strs = [input().split() for _ in range(n)]

    for s in strs:
        if len(s) >= 2:
            if s[0].lower() == "simon" and s[1].lower() == "says":
                print(" ".join(s[2:]))


if __name__ == "__main__":
    main()
