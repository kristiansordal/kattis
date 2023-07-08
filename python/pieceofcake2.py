def main():
    n, h, v = map(int, input().split())
    h1 = n - h
    v1 = n - v

    i = max(h, h1)
    j = max(v, v1)

    print(i * j * 4)


if __name__ == "__main__":
    main()
