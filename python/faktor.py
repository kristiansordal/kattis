import math


def main():
    x, y = map(float, input().split())
    y -= 0.999999

    f = math.ceil(x * y)
    print(f)


if __name__ == "__main__":
    main()
