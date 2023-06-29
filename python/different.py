import sys

nums = [abs(int(l.split()[0]) - int(l.split()[1])) for l in sys.stdin.readlines()]
for n in nums:
    print(n)
