n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    if(i not in c):
        c.append(i)
for i in c:
    d.append(i)
    d.append(l.count(i))
print(*d)