# dp = [(None, None) for _ in range(price + 1)]
# dp[0] = (0, 0)  # It takes 0 coins/bills to pay $0

# # Sort the denominations for easier processing
# denominations.sort(reverse=True)

# for coin in denominations:
#     for current_price in range(coin, price + 1):
#         if dp[current_price - coin][0] is not None:
#             # Calculate new values if we take this coin
#             new_amount = dp[current_price - coin][0] + coin
#             new_number_of_coins = dp[current_price - coin][1] + 1

#             # If this is the first time we can pay this amount or if this new method uses fewer coins
#             # or the same number of coins but pays a smaller amount, update the dp table
#             if (
#                 dp[current_price][0] is None
#                 or new_number_of_coins < dp[current_price][1]
#                 or (
#                     new_number_of_coins == dp[current_price][1]
#                     and new_amount < dp[current_price][0]
#                 )
#             ):
#                 dp[current_price] = (new_amount, new_number_of_coins)

# # Find the minimum payment that is equal or exceeds the price
# for pay in range(price, len(dp)):
#     if dp[pay][0] is not None:
#         return dp[pay]


# return None, None  # No solution found
def knapsack(v, W):
    n = len(v)
    dp = [[None, None] for _ in range(W + 1)]
    dp[0] = [0, 0]  # type: ignore

    v = sorted(v, reverse=True)

    for coin in v:
        for p in range(coin, W + 1):
            new_amount = dp[p - coin][0] + coin
            new_coin_count = dp[p - coin][1] + 1

            if dp[p] = [None,None]  or new_coin_count < dp[p][1] or ()
            # if (
            #     dp[current_price][0] is None
            #     or new_number_of_coins < dp[current_price][1]
            #     or (
            #         new_number_of_coins == dp[current_price][1]
            #         and new_amount < dp[current_price][0]
            #     )
            # ):
            #     dp[current_price] = (new_amount, new_number_of_coins)

    print(f"{dp[-1][-1][0] } {dp[-1][-1][1]}")


def main():
    t = int(input())

    for _ in range(t):
        to_pay = int(input())
        n = int(input())
        vals = [int(input()) for _ in range(n)]
        knapsack(vals, to_pay)


if __name__ == "__main__":
    main()
