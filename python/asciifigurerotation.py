transpose = lambda b: list(map(list, zip(*b)))
flip = lambda b: [row[::-1] for row in b]
chars = {"+": "+", "-": "|", "|": "-", " ": " "}

n = int(input())
while n != 0:
    figure = [list(input()) for _ in range(n)]
    m = max(len(l) for l in figure)
    figure = [l + [" "] * (m - len(l)) for l in figure]
    figure = flip(transpose(figure))
    figure = [[chars[x] for x in l] for l in figure]

    for l in figure:
        while l[-1] == " ":
            l.pop()
        print("".join(l))
    n = int(input())
    if n != 0:
        print()
