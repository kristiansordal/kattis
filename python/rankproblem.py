def main():
    t, m = map(int, input().split())
    ranks = [i for i in range(1, t + 1)]

    if t == 1:
        print("T1")
        exit()
    for _ in range(m):
        ti, tj = input().split()
        n = ranks.index(int(ti[1:]))
        m = ranks.index(int(tj[1:]))

        if n > m:
            for i in range(m, n):
                ranks[i] = ranks[i + 1]
            ranks[n] = int(tj[1:])

    s = ["T" + str(i) for i in ranks]
    print(" ".join(s))


if __name__ == "__main__":
    main()
