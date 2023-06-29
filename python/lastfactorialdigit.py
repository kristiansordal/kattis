import math
import sys


def main():
    ints = [int(x) for x in sys.stdin.readlines()]
    for x in ints[1:]:
        print(str(math.factorial(x))[-1])


if __name__ == "__main__":
    main()
