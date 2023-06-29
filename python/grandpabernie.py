import sys
def main():
    input = [x.strip() for x in sys.stdin]
    countries = {}
    num1 = int(input[0])
    num2 = num1 + int(input[num1 + 1])

    for x in range(1, num1 + 1):
        curr = input[x].split(' ')
        if curr[0] in countries.keys():
            countries[curr[0]].append(int(curr[1]))
        else:
            countries[curr[0]] = [int(curr[1])]

    map(sorted, countries.keys())

    for x in range(num1 + 2, num2 + 2):
        curr = input[x].split(' ')
        print(countries[curr[0]][int(curr[1]) - 1])


  
if __name__ == '__main__':
    main()
