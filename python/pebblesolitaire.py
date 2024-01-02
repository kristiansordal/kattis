def get_moves(game, move):
    start = 0
    while start < len(game):
        start = game.find(move, start)
        if start == -1:
            break
        yield start
        start += 1


def solve(game, memo):
    s = "".join(game)
    if s in memo:
        return s.count("o")
    else:
        memo.add(s)

    avail_moves = list(get_moves(s, "oo-"))
    avail_moves += list(get_moves(s, "-oo"))

    if not avail_moves:
        return game.count("o")

    possible_games = []
    for move in avail_moves:
        new_game = game[:]
        new_game[move + 1] = "-"

        # oo- -> --o
        if new_game[move] == "o":
            new_game[move] = "-"
            new_game[move + 2] = "o"
        # -oo -> o--
        else:
            new_game[move] = "o"
            new_game[move + 2] = "-"
        possible_games.append(new_game)

    return min(solve(g, memo) for g in possible_games)


def main():
    t = int(input())
    cases = [list(input().strip()) for _ in range(t)]
    for c in cases:
        print(solve(c, set()))


if __name__ == "__main__":
    main()
