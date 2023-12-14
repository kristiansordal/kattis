def find_lexicographically_smallest(s):
    smallest = s
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        smallest = min(smallest, rotated)
    return reversed(smallest)


def main():
    n = int(input())
    names = []

    for _ in range(n):
        name = input().strip()
        if len(name) >= 5 and len(set(name)) == len(name):
            smallest_rotation = find_lexicographically_smallest(name)
            names.append(smallest_rotation)

    for result in names:
        print("".join(list(result)))


if __name__ == "__main__":
    main()
