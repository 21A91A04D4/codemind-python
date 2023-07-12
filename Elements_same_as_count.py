n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
s=0
for i in l:
    if(l.count(i) == i):
        c.append(i)
        s+=1
for i in c:
    if(i not in d):
        d.append(i)
if(s == 0):
    print(-1)
else:
    print(*d)