n=int(input())
l=list(map(int,input().split()))
s=int(input())
c=[]
d=[]
e=0
for i in l:
    if(l.count(i) == s):
        c.append(i)
        e+=1
for i in c:
    if(i not in d):
        d.append(i)
if(e == 0):
    print(-1)
else:
    print(*d)