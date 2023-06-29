import sys
def main():
    knapsack = [(int(m.split(' ')[0]), int(m.split(' ')[1])) for m in sys.stdin.readlines()]
    print(knapsack)

    m = []
    for j in range(max(x[0] for x in knapsack)):




main()

# // Input:
# // Values (stored in array v)
# // Weights (stored in array w)
# // Number of distinct items (n)
# // Knapsack capacity (W)
# // NOTE: The array "v" and array "w" are assumed to store all relevant values starting at index 1.

# array m[0..n, 0..W];
# for j from 0 to W do:
#     m[0, j] := 0
# for i from 1 to n do:
#     m[i, 0] := 0

# for i from 1 to n do:
#     for j from 0 to W do:
#         if w[i] > j then:
#             m[i, j] := m[i-1, j]
#         else:
#             m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])
#         

