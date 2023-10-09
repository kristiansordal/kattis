def convert(romans):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for r in romans:
        num = 0
        r, curr = r[1:], d[r[0]]
        num += curr
        while r:
            prev = curr
            r, curr = r[1:], d[r[0]]

            if prev >= curr:
                num -= curr
            else:
                num += curr
        print(num)


def main():
    n = int(input())

    romans = []
    for _ in range(n):
        s = input()
        romans.append(list(reversed(s)))
    convert(romans)


main()
