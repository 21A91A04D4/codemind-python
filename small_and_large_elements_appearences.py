s=input()
l=list(s)
c=[]
for i in l:
    if(i != " "):
        c.append(i)
print(min(c),c.count(min(c)),max(c),c.count(max(c)))