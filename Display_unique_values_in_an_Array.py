n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if l.count(i)==1:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(*d)