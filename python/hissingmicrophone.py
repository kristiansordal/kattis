def main():
    x = input()
    hiss = False
    for i in range(0, len(x) - 1):
        if x[i] == "s" and x[i + 1] == "s":
            hiss = True
            break
    if hiss:
        print("hiss")
    else:
        print("no hiss")


if __name__ == "__main__":
    main()
