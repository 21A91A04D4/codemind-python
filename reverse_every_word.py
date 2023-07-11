n=input().split()
c=[]
for i in n:
    l=list(i)
    l.reverse()
    s=("".join(l))
    c.append(s)
print(*c)