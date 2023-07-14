n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i == l.count(i) and i not in c):
        c.append(i)
s=sum(c)
if(s == 0):
    print(-1)
else:
    t=s/len(c)
    print("%.2f"%t)