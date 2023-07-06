n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in range(len(l)):
    if(l[i] < a or l[i] > b):
        c.append(l[i])
    else:
        d.append(l[i])
if(len(d) == 0):
    print("-1")
else:
    print(max(d))