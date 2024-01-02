def edit_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])

    return 1 + min(
        edit_distance(s1[1:], s2),
        edit_distance(s1, s2[1:]),
        edit_distance(s1[1:], s2[1:]),
    )


n, m = map(int, input().split())
start = input().strip()
end = input().strip()
lucky = [input().strip() for _ in range(m)]
used = set()

print(start)
print(end)
print(lucky)
curr = start
steps = 0
order = [start]
while curr != end:
    print(curr)
    for l in lucky:
        if (
            l not in used
            and edit_distance(curr, l) == 1
            and edit_distance(curr, end) >= edit_distance(l, end)
        ):
            diffs = [abs(int(x) - int(y)) for x, y in zip(curr, l)]
            if all([d <= 1 for d in diffs]):
                curr = l
                used.add(curr)
                steps += 1
                order.append(curr)
                break
    if edit_distance(curr, end) == 1:
        steps += 1
        curr = end
    if curr == start:
        print("Neibb")
        exit()
print(steps)
for o in order:
    print(o)
print(end)
