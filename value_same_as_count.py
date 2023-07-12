n=int(input())
l=list(map(int,input().split()))
c=[]
d=0
for i in l:
    if(i not in c):
        c.append(i)
for i in c:
    if(i == l.count(i)):
        d+=1
print(d)