n=int(input())
l=list(map(int,input().split()))
s=0
c=[]
for i in l:
    i=str(i)
    l1=i[::-1]
    c.append(l1)
for i in range(n):
    if(l[i] == int(c[i])):
        s+=1
print(s)