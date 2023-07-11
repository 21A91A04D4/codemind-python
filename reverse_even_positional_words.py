n=input().split()
c=[]
for i in range(len(n)):
    s=n[i]
    if(i % 2 == 0):
        a=list(s)
        a.reverse()
        b=("".join(a))
        c.append(b)
    else:
        c.append(s)
print(*c)