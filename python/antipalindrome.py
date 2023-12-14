def palindrome(s):
    if s == s[::-1]:
        return True
    w = 2
    while w < len(s):
        for i in range(len(s) - w + 1):
            sub = s[i : i + w]
            if sub == sub[::-1]:
                return True
        w += 1
    return False


def main():
    s = input().strip()

    # for t in testcases:
    s = "".join(char.lower() for char in s if char.isalpha())

    if palindrome(s.lower()):
        print("Palindrome")
    else:
        print("Anti-palindrome")


if __name__ == "__main__":
    main()
