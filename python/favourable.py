def find(m, leaves, s):
    if s in leaves:
        return leaves[s]

    else:
        total = 0
        l = m[s]
        total += find(m, leaves, l[0]) + find(m, leaves, l[1]) + find(m, leaves, l[2])
        leaves[s] = total
        return total


def main():
    t = int(input())

    for _ in range(t):
        s = int(input())
        leaves = {}
        m = {}

        for _ in range(s):
            d = input().split()
            if d[1] == "favourably":
                leaves[d[0]] = 1
            elif d[1] == "catastrophically":
                leaves[d[0]] = 0
            else:
                m[d[0]] = d[1:]

        print(find(m, leaves, "1"))


if __name__ == "__main__":
    main()
