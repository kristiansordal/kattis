from math import floor


def main():
    n = int(input())
    speeds = []
    for _ in range(n):
        x, y = map(int, input().split())
        speeds.append((x, y))

    s = []
    for i in range(len(speeds) - 1):
        v = floor((speeds[i + 1][1] - speeds[i][1]) / (speeds[i + 1][0] - speeds[i][0]))
        s.append(v)

    print(max(s))


if __name__ == "__main__":
    main()
