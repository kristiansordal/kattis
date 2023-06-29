import sys
from itertools import groupby


def main():
    typed = sys.stdin.readline()
    sticky = sys.stdin.readline()

    notSticky = list(
        filter(lambda x: len(x) > 1, ([list(group) for _, group in groupby(typed)]))
    )
    keys = filter(
        lambda x: len(x) > 1 and list(x) not in notSticky,
        ([list(group) for _, group in groupby(sticky)]),
    )

    keys = set().union(*list(map(set, list(keys))))

    print("".join(list(keys)))


if __name__ == "__main__":
    main()
