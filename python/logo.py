import sys
import math


def updatePos(rot, hyp):
    x, y = 0, 0
    if rot >= 0 and rot < 90:
        x = math.cos(math.radians(rot)) * hyp
        y = math.sin(math.radians(rot)) * hyp
        return (x, y)

    elif rot >= 90 and rot < 180:
        tempRot = 180 - rot
        x = math.cos(math.radians(tempRot)) * hyp
        y = math.sin(math.radians(tempRot)) * hyp
        return (-x, y)

    elif rot >= 180 and rot < 270:
        tempRot = 270 - rot
        y = math.cos(math.radians(tempRot)) * hyp
        x = math.sin(math.radians(tempRot)) * hyp
        return (-x, -y)

    elif rot >= 270 and rot < 360:
        tempRot = 360 - rot
        x = math.cos(math.radians(tempRot)) * hyp
        y = math.sin(math.radians(tempRot)) * hyp
        return (x, -y)

    return (x, y)


def main():
    t = int(input())
    for _ in range(t):
        c = int(input())
        pos = [0, 0]
        rotation = 0
        for _ in range(c):
            dir, unit = sys.stdin.readline().split()
            unit = int(unit)

            if dir == "fd":
                (x, y) = updatePos(rotation, unit)
                pos = [pos[0] + x, pos[1] + y]
            elif dir == "bk":
                (x, y) = updatePos(rotation, unit)
                pos = [pos[0] - x, pos[1] - y]
            elif dir == "lt":
                rotation = (rotation + unit) % 360
            elif dir == "rt":
                rotation = (rotation - unit) % 360

        d = math.sqrt((pos[0] ** 2) + (pos[1] ** 2))
        print(round(d))


if __name__ == "__main__":
    main()
