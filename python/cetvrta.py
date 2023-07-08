def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x, y = list({x1, y1, x2, y2, x3, y3})
    ps = {(x1, y1), (x2, y2), (x3, y3)}

    if (x, x) not in ps:
        print(x, " ", x)
    elif (y, y) not in ps:
        print(y, " ", y)
    elif (x, y) not in ps:
        print(x, " ", y)
    else:
        print(y, " ", x)


if __name__ == "__main__":
    main()
