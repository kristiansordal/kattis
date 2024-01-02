# fmt: off
b=input
p=print
while(n:=int(b()))!=0:
 v=[]
 for i in range(n):
  x,y=map(int,b().split())
  v.append((x,y))
 a=0.0
 for i in range(n-1):
  a+=v[i][0]*v[i+1][1]-v[i+1][0]*v[i][1]
 a+=v[-1][0]*v[0][1]-v[0][0]*v[-1][1]
 print("CW"if a<0 else"CCW",format(abs(a)/2,".1f"))
