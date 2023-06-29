import sys


def main():
    kitten = int(sys.stdin.readline())
    # branches = [[int(x) for x in l.strip().split()] for l in sys.stdin.readlines()]
    branches = [{l[0].strip: l[1:]} for l in sys.stdin.readlines()]
    print(branches)


if __name__ == "__main__":
    main()
