s=input().split()
c=[]
for i in s:
    c.append(min(i))
    c.append(max(i))
print(*c)