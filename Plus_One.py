n=int(input())
l=list(map(int,input().split()))
s=""
for i in range(len(l)):
    s+=str(l[i])
k=int(s)+1
k=str(k)
l=list(k)
print(*l)