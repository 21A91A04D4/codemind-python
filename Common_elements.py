n,m=map(int,input().split())
s=list(map(int,input().split()))
l=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in s:
    if(i not in a):
        a.append(i)
for j in l:
    if(j not in b):
        b.append(j)
for k in a:
    if(k in b):
        c.append(k)
print(*c)