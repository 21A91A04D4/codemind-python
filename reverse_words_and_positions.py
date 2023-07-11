n=input().split()
n.reverse()
c=[]
for i in n:
    s=i[::-1]
    c.append(s)
print(*c)