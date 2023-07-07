n,m=map(int,input().split())
s=list(map(int,input().split()))
l=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in s:
    if(i not in c):
        c.append(i)
for i in l:
    if(i not in d):
        d.append(i)
for i in c:
    if(i not in d):
        e.append(i)
for i in d:
    if(i not in c):
        e.append(i)
print(len(e))