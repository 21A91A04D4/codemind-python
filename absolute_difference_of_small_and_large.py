s=input().split()
c=[]
for i in s:
    a=ord(max(i)) - ord(min(i))
    c.append(a)
print(*c)