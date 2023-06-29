def main():
    x = input()
    r = []

    for c in x:
        if c == "e":
            r.append("e" * 2)
        else:
            r.append(c)

    print("".join(r))


if __name__ == "__main__":
    main()
