n=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in range(len(l)):
    t=l.count(s)
print(t)