n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(l)):
    if(i % 2 == 0):
        e.append(l[i])
    else:
        o.append(l[i])
if(sum(e)-sum(o) == 0):
    print("YES")
else:
    print("NO")
