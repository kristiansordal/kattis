import sys


def main():
    qwerty_mapping = {
        "Q": None,
        "W": "Q",
        "E": "W",
        "R": "E",
        "T": "R",
        "Y": "T",
        "U": "Y",
        "I": "U",
        "O": "I",
        "P": "O",
        "A": None,
        "S": "A",
        "D": "S",
        "F": "D",
        "G": "F",
        "H": "G",
        "J": "H",
        "K": "J",
        "L": "K",
        "Z": None,
        "X": "Z",
        "C": "X",
        "V": "C",
        "B": "V",
        "N": "B",
        "M": "N",
        ",": "M",
        ";": "L",
        "[": "P",
        "/": ".",
        ".": ",",
        " ": " ",
        "\\": "]",
        "]": "[",
        "1": "`",
        "2": "1",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
        "0": "9",
        "-": "0",
        "=": "-",
        "'": ";",
    }

    x = [x.strip() for x in sys.stdin.readlines()]

    for l in x:
        s = ""
        for c in l:
            s += qwerty_mapping[c]
        print(s)


if __name__ == "__main__":
    main()
