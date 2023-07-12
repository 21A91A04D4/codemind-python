n=input()
s=n.lower()
l=list(s)
c=[]
for i in l:
    if(l.count(i) == 1 and i != " "):
        c.append(i)
c.sort()
print("".join(c))