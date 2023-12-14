def main():
    h, w = map(int, input().split())
    # grid = [input().strip() for _ in range(h)]

    forces = []
    base = []
    for i in range(h):
        l = input().strip()
        for j in range(w):
            if l[j] != ".":
                forces.append(j)
                if i == h - 1:
                    base.append(j)

    left, right = base[0], base[-1]
    avg_force_pos = sum(forces) / len(forces)

    if avg_force_pos >= left - 0.5 and avg_force_pos <= right + 0.5:
        print("balanced")
    elif avg_force_pos < left - 0.5:
        print("left")
    else:
        print("right")


if __name__ == "__main__":
    main()
