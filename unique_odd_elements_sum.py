n=int(input())
l=list(map(int,input().split()))
c=[]
b=[]
for i in l:
    if(i not in c):
        c.append(i)
for i in c:
    if(i % 2 !=0):
        b.append(i)
print(sum(b))