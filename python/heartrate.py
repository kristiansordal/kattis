def main():
    n = int(input())

    for _ in range(n):
        b, p = map(float, input().split())

        bpm = 60 * b / p
        s = bpm / 60
        var = bpm - (bpm / s)

        print(bpm, " ", s, " ", var)

        print(round(bpm - var, 4), " ", round(bpm, 4), " ", round(bpm + var, 4))


if __name__ == "__main__":
    main()
