def turn(animal_dict, prev):
    candidates = animal_dict.get(prev[-1], [])

    if (len(candidates)) == 0:
        return "?"

    for a in candidates:
        d = animal_dict.get(a[-1], [])

        # if a in d:
        #     d.remove(a)

        if len(d) == 0:
            return "".join([a, "!"])

    return list(candidates)[0]


def main():
    prev = input()
    x = int(input())
    animal_dict = {}
    for _ in range(x):
        animal = input().strip()
        animal_dict.setdefault(animal[0], set()).add(animal)

    print(turn(animal_dict, prev))


if __name__ == "__main__":
    main()
