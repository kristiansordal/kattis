def main():
    n = int(input())
    l = list(map(int, input().split()))
    c = list(sorted(l))
    n = len(list(filter(lambda x: x[0] != x[1], zip(l, c))))

    print(n)


main()
