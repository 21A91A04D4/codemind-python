n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=c*2+int(i)
print(c)