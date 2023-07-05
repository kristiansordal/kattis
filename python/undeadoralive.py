def main():
    s = input()

    if s.find(":(") != -1 and s.find(":)") != -1:
        print("double agent")
    elif s.find(":)") != -1:
        print("alive")
    elif s.find(":(") != -1:
        print("undead")
    else:
        print("machine")


if __name__ == "__main__":
    main()
