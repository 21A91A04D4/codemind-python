s=input().split()
c=[]
d=[]
for i in s:
    c.append(ord(min(i)))
    d.append(ord(max(i)))
print(sum(d) - sum(c))