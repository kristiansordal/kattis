def main():
    x = input()
    x = filter(lambda x: x.isupper(), x)
    print("".join(list(x)))


if __name__ == "__main__":
    main()
