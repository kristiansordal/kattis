def main():
    x, y = map(int, input().split())

    scores = {}

    for i in range(x):
        for j in range(y):
            if i + j not in scores:
                scores[i + j] = 1
            else:
                scores[i + j] += 1

    max = 0
    mv = 0
    for k in scores:
        if scores[k] > mv:
            max = k
            mv = scores[k]

    maxVs = []
    for k in scores:
        if scores[k] == max:
            maxVs.append(k)

    for v in maxVs:
        print(v)
    # print("".join(*sorted(maxVs)))


if __name__ == "__main__":
    main()
