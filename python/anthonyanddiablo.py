from math import pi


def main():
    a, n = map(float, input().split())

    r = n / (2 * pi)
    max_a = pi * r * r

    if max_a >= a:
        print("Diablo is happy!")
    else:
        print("Need more materials!")


if __name__ == "__main__":
    main()
