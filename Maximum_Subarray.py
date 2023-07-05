n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        s=sum(l[i:j+1])
        c.append(s)
print(max(c))