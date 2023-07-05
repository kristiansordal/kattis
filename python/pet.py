def main():
    ps = []
    for i in range(5):
        p = sum(map(int, input().split()))
        ps.append((p, i + 1))
    m = max(ps)
    print(m[1], " ", m[0])


if __name__ == "__main__":
    main()
