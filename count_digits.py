n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i >= 0):
        s=str(i)
        s=list(s)
        s=len(s)
        c.append(s)
    else:
        s=str(i)
        s=list(s)
        s=len(s)-1
        c.append(s)
print(*c)