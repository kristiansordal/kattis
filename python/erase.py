import sys

sweep = int(sys.stdin.readline())

bits = [x.strip() for x in sys.stdin.readlines()]

success = False
if sweep % 2 == 0:
    success = bits[0] == bits[1]
else:
    success = not any(map(lambda x: x[0] == x[1], zip(bits[0], bits[1])))


if success:
    print("Deletion succeeded")
else:
    print("Deletion failed")
