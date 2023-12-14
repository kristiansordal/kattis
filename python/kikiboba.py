from collections import Counter


def main():
    s = Counter(input())

    if not s["k"] and not s["b"]:
        print("none")
    elif s["k"] == s["b"]:
        print("boki")
    elif s["k"] > s["b"]:
        print("kiki")
    else:
        print("boba")


if __name__ == "__main__":
    main()
