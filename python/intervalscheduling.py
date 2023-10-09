def interval_schedule(intervals):
    s = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= s[len(s) - 1][1]:
            s.append(intervals[i])

    return len(s)


def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((s, e))

    intervals = sorted(intervals, key=lambda x: (x[1], x[0]))

    print(interval_schedule(intervals))


if __name__ == "__main__":
    main()
