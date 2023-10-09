def main():
    x1, y1, x2, y2 = map(float, input().split())

    l = max(x1, x2) - min(x1, x2)
    w = max(y1, y2) - min(y1, y2)

    print(abs(l) * abs(w))


if __name__ == "__main__":
    main()
