import sys


def longestsubsequence(s):
    l = 0
    m = [-1 for _ in range(len(s) + 1)]
    p = [-1 for _ in range(len(s))]

    for i in range(len(s)):
        lo = 1
        hi = l + 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if s[m[mid]] >= s[i]:
                hi = mid
            else:
                lo = mid + 1

        nl = lo

        p[i] = m[nl - 1]
        m[nl] = i

        if nl > l:
            l = nl

    k = m[l]
    seq = [-1 for _ in range(l)]
    for i in range(l - 1, -1, -1):
        seq[i] = k
        k = p[k]

    return l, seq


def main():
    n = sys.stdin.read().split("\n")

    for i in range(0, len(n) - 1, 2):
        s = [int(x) for x in n[i + 1].split()]
        m, s = longestsubsequence(s)
        print(m)
        print(" ".join(map(str, s)))


if __name__ == "__main__":
    main()
