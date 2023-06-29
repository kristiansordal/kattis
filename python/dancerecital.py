def find_min(curr, routines, qc):
    for r in routines:
        min_dup, min_routine = find_duplicates(curr, r)


def find_duplicates(x, y):
    dup = 0

    for c in y:
        if c in x:
            dup += 1
    return dup, y


def main():
    dances = int(input())
    routines = []
    for _ in range(dances):
        routines.append(input())

    qc = []
    q = 0
    for i in range(len(routines)):
        qc.append(find_min(routines[i], routines.remove(i), 0))

    print(min(qc))


if __name__ == "__main__":
    main()
