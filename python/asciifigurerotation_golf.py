i=input
p=print
n=int(i())
while n:
 f=[list(i())for _ in" "*n]
 for l in [[{"+":"+","-":"|","|":"-"," ":" "}[x]for x in l]for l in[r[::-1]for r in[*zip(*[l+[" "]*(max(len(l)for l in f)-len(l))for l in f])]]]:
  p("".join(l).rstrip())
 n=int(i())
 if n:p()
