n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(l.count(i) == 2):
        c.append(i)
        break
print(*c)