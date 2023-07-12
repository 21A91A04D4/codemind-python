n=input()
s=n.lower()
l=list(s)
c=0
for i in l:
    if(l.count(i) == 1 and i != " "):
        c+=1
print(c)