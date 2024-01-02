# fmt: off
i=input
n=int(i())
while n:
 f=[[*i()]for _ in' '*n]
 for l in zip(*[l+[' ']*(max(map(len,f))-len(l))for l in f][::-1]):print(''.join({'+':'+','-':'|','|':'-',' ':' '}[x]for x in l).rstrip())
 n=int(i())
 if n:print()
