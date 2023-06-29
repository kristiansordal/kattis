import debugpy


def thought(x):
    ops = ["+", "-", "//", "*"]
    solution = False
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                if eval(f"4{op1}4{op2}4{op3}4") == x:
                    return f"4 {op1} 4 {op2} 4 {op3} 4 = {x}".replace("//", "/")

    if not solution:
        return "no solution"


def main():
    debugpy.listen(5678)
    debugpy.wait_for_client()
    cases = int(input())
    for _ in range(cases):
        num = int(input())
        print(thought(num))


if __name__ == "__main__":
    main()
