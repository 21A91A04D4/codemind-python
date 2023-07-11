n=input()
l=list(n)
c=[]
d=0
for i in l:
    if(l.count(i) == 1):
        c.append(i)
        d+=1
if(d == 0):
    print(-1)
else:
    print(c[0])