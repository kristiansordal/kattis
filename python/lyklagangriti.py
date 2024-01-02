from collections import deque


class PasswordEntry:
    def __init__(self, entry):
        self.entry = deque(list(entry))
        self.cursor = 0
        self.password = []

    def solve(self):
        while self.entry:
            key = self.entry.popleft()
            if key == "L":
                self.cursor -= 1
            elif key == "R":
                self.cursor += 1
            elif key == "B":
                self.password.pop(self.cursor - 1)
                self.cursor -= 1
            else:
                self.password.insert(self.cursor, key)
                self.cursor += 1

        print("".join(self.password))


def main():
    entry = input().strip()
    password_entry = PasswordEntry(entry)
    password_entry.solve()


if __name__ == "__main__":
    main()
