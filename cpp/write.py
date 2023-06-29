import random
def main():
    f = open("test.txt", "a")

    for i in range(0, 100001):
        if i == 0:
            f.write("100000\n")
        else:
            f.write(f'player{i} {random.randint(0, 2000000000)} {random.randint(0,2000000000)} {random.randint(0,2000000000)}\n')


if __name__ == '__main__':
    main()
