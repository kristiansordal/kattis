def pricing(tickets, estimates):
    weeks = len(estimates)

    dp = [[(x * y, tickets - y, x) for x, y in estimates[0]]]

    for i in range(1, weeks):
        if len(dp) > i - 1:
            potential_revenues = []

            for opt in dp[i - 1]:
                prev_opt_revenue = opt[0]
                available_tickets = opt[1]

                if available_tickets <= 0:
                    continue

                for e in estimates[i]:
                    revenue = 0
                    if available_tickets <= e[1]:
                        revenue = e[0] * available_tickets
                    else:
                        revenue = e[0] * e[1]

                    opt_revenue = revenue + prev_opt_revenue
                    price_week_1 = opt[2]

                    potential_revenues.append(
                        (opt_revenue, max(0, available_tickets - e[1]), price_week_1)
                    )
            if potential_revenues:
                dp.append(potential_revenues)

    m = max(dp[-1])
    price = m[2]

    for e in dp[-1]:
        if e[2] < price and e[0] == m[0]:
            price = e[2]

    print(m[0])
    print(price)


def main():
    n, w = map(int, input().split())
    estimates = []
    for _ in range(w + 1):
        k = list(map(int, input().split()))
        prices = k[1 : k[0] + 1]
        sales = k[-k[0] :]

        estimates.append(list(zip(prices, sales)))

    pricing(n, estimates)


if __name__ == "__main__":
    main()
