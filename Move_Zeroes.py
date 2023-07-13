n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    if(i != 0):
        c.append(i)
    else:
        d.append(i)
print(*(c+d))