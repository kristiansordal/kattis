import random


def generate_test_case():
    n = random.randint(2, 100)
    m = random.randint(0, n * (n - 1) // 2)
    x = random.randint(1, n)
    y = random.randint(1, n)
    while x == y:
        y = random.randint(1, n)

    test_case = f"{n} {m} {x} {y}\n"

    a = random.randint(1, n)
    b = random.randint(1, n)
    w = random.randint(1, 1_000_000)
    c = random.randint(1, 2)
    test_case += f"{x} {a} {w} {c}\n"
    w = random.randint(1, 1_000_000)
    c = random.randint(1, 2)
    test_case += f"{y} {b} {w} {c}\n"

    for _ in range(m):
        a = random.randint(1, n)
        b = random.randint(1, n)
        w = random.randint(1, 1_000_000)
        c = random.randint(1, 2)

        test_case += f"{a} {b} {w} {c}\n"

    return test_case


def main():
    content = generate_test_case()
    with open("fot.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
