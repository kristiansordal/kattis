from random import randint, choice

size = input("Problem size: ")
n, q = map(int, size.split())

with open(f'test-{n}-{q}' , "w") as f:
    f.write(size + "\n")
    for _ in range(q):
        f.write(f'{choice(["?", "="])} {randint(0, n-1)} {randint(0, n-1)}\n')
