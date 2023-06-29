import sys

x = int(input())
nums = [int(x) for x in sys.stdin.readlines()]

print(sum(nums) - (x - 1))
