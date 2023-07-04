a,b=map(int,input().split())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(len(l)):
    for j in range(i,len(l)):
        d=sum(l[i:j+1])
        s.append(d)
for i in s:
    if(i == b):
        c+=1
print(c)