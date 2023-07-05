n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    s=l[i]**0.5
    if(s == int(s)):
        c.append(l[i])
print(sum(c))