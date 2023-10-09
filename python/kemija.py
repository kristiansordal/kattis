def main():
    words = input().split()

    newWords = []
    for w in words:
        nw = ""
        i = 0
        while i < len(w):
            if i < len(w) - 2:
                if w[i] in "aeiou" and w[i + 1] == "p" and w[i + 2] == w[i]:
                    nw += w[i]
                    i += 2
            else:
                nw += w[i]
                i += 1

        newWords.append(nw)

    print(newWords)


if __name__ == "__main__":
    main()
