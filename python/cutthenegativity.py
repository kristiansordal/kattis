class Flight:
    def __init__(self, f, t, c):
        self.f = f
        self.t = t
        self.c = c

    def __str__(self):
        return f"{self.f} {self.t} {self.c}"

    def __lt__(self, obj):
        if self.f < obj.f:
            return self.f < obj.f
        return self.t < obj.t


def main():
    n = int(input())

    adj = []
    for _ in range(n):
        x = map(int, input().split())
        adj.append(list(x))

    flights = []
    for i in range(n):
        for j in range(n):
            if adj[j][i] > -1:
                flights.append(Flight(j + 1, i + 1, adj[j][i]))

    flights = sorted(flights)
    print(len(flights))
    for f in flights:
        print(f)


if __name__ == "__main__":
    main()
