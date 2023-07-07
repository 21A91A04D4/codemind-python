n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
for i in l:
    s=0
    for j in range(1,i+1):
        if(i % j == 0):
            s+=1
    if(s == 2):
        c.append(i)
t=0
for i in range(len(c)):
    if(c[i] <= k):
        t+=1
print(t)