import itertools

string = input()
y = itertools.dropwhile(lambda x: x != "a", string)
print("".join(list(itertools.chain(*y))))
