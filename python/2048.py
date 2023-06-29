import sys

def move(nums):
    m = nums.pop()[0]

    if m == 0:
        for line in nums:
            if len(set(line)) == len(line):
                continue
            else:
                prevZero = False
                for i in range (0, len(line)):
                    for j in range(i + 1, len(line)):
                        if line[j] == line[i] or line[j] == 0:


                # for i in range(0, len(line) - 1):





def main():
    nums = [[int(x) for x in l.strip().split()] for l in sys.stdin] 

main()
