keymap = {
    "clank": "a",
    "bong": "b",
    "click": "c",
    "tap": "d",
    "poing": "e",
    "clonk": "f",
    "clack": "g",
    "ping": "h",
    "tip": "i",
    "cloing": "j",
    "tic": "k",
    "cling": "l",
    "bing": "m",
    "pong": "n",
    "clang": "o",
    "pang": "p",
    "clong": "q",
    "tac": "r",
    "boing": "s",
    "boink": "t",
    "cloink": "u",
    "rattle": "v",
    "clock": "w",
    "toc": "x",
    "clink": "y",
    "tuc": "z",
    "whack": " ",
}

n = int(input())

s = []
caps = False
for _ in range(n):
    char = input().strip()
    if keymap.get(char):
        if caps:
            s.append(keymap[char].upper())
        else:
            s.append(keymap[char])
    else:
        if char in ["bump", "dink"]:
            caps = not caps
        if char == "thumb" and caps:
            capse = not caps
        if char == "pop":
            s.pop()
print("".join(s))
