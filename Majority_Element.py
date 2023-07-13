n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    s=l.count(i)
    c.append(s)
t=max(c)
for i in l:
    if(l.count(i) == t and i not in d):
        d.append(i)
print(*d)