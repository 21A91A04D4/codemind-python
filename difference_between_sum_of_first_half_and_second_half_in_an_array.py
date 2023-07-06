n=int(input())
l=list(map(int,input().split()))
c=l[:len(l)//2]
d=l[len(l)//2:]
a=sum(c)
b=sum(d)
if(a > b):
    print(a-b)
else:
    print(b-a)