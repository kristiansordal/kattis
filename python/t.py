import random

with open("t.txt", "w") as file:
    n = random.randrange(1, 300)
    w = random.randrange(0, 10)

    file.write(f"{n} {w}\n")

    for _ in range(w + 1):
        k = random.randrange(1, 10)
        file.write(f"{k} ")

        for _ in range(k):
            x = random.randrange(0, 500)
            file.write(f"{x} ")

        for _ in range(k):
            x = random.randrange(0, n)
            file.write(f"{x} ")
        file.write("\n")

print("File 't.txt' has been created.")
