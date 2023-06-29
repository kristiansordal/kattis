import random

cases = 1000
points = set()
with open("t.txt", "a") as f:
    for c in range(cases):
        num = random.randrange(10000)
        f.write(f"{num}\n")
        for _ in range(num):
            x = random.randrange(-10000, 10000)
            y = random.randrange(-10000, 10000)
            if (x, y) not in points:
                f.write(f"{x} {y}\n")

        points.clear()

    f.write("0")
