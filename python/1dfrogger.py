import sys

def game(inp):
    squares = inp[0][0]
    start = inp[0][1]
    goal = inp[0][2]
    seen = [False]*len(inp[1])
    board = inp[1]
    c = start - 1
    h = 0

    while True:
        if board[c] == goal:
            return ('magic', h)
        elif c > squares - 1:
            return ('right', h)
        elif c < 0:
            return ('left', h)
        elif board[c] >= 0:
            if seen[c] == True:
                return ('cycle', h)
            
            seen[c] = True
            h += 1
            c += board[c]
        elif board[c] < 0:
            if seen[c] == True:
                return ('cycle', h)
            
            seen[c] = True
            h += 1
            c -= abs(board[c])
    

def main():
    inp = [[int(x) for x in l.strip().split()] for l in sys.stdin]
    result = game(inp)
    print(result[0])
    print(result[1])


main()
