from itertools import takewhile

transpose = lambda b: list(map(list, zip(*b)))
flip = lambda b: [row[::-1] for row in b]
board = [list(map(int, input().split())) for _ in range(4)]
move = int(input())
rotations = [(0, 0), (3, 1), (2, 2), (1, 3)]

for _ in range(rotations[move][0]):
    board = flip(transpose(board))

for i, l in enumerate(board):
    nl = []
    while l:
        s = list(takewhile(lambda x: x == l[0] or x == 0, l))
        while len([x for x in s if x != 0]) > 2:
            s = s[:-1]
        if sum(s) != 0:
            l = l[len(s) :]
            nl.append(sum(s))
        else:
            l.pop(0)
    nl += [0] * (4 - len(nl))
    board[i] = nl

for _ in range(rotations[move][0]):
    board = transpose(flip(board))

for l in board:
    print(" ".join(list(map(str, l))))
