n,m=map(int,input().split())
s=list(map(int,input().split()))
l=list(map(int,input().split()))
c=[]

for i in s:
    if(i not in l):
        c.append(i)
for i in l:
    if(i not in s):
        c.append(i)
print(*c)