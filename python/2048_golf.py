# fmt: off
from itertools import takewhile as t
a,b,c,d,e=[],[],input,len,str
for _ in'1234':a+=[[int(x)for x in b().split()]]
m=int(b())
r=[(0,0),(3,1),(2,2),(1,3)]
for _ in[0]*r[m][0]:a=[x[::-1]for x in zip(*a)]
for i in range(4):
 q,l=[],[*a[i]]
 while l:
  s=[*t(lambda x:x==l[0]or x==0,l)]
  while d([x for x in s if x]):s.pop()
  if sum(s):l=l[d(s):];q+=[sum(s)]
  else:l.pop(0)
 a[i]=q+[0]*(4-d(q))
for _ in[0]*r[m][0]:a=[x[::-1]for x in zip(*a)]
for l in a:print(" ".join(map(e,l)))
