n=int(input())
l=list(map(int,input().split()))
a=l[:len(l)//2]
b=l[len(l)//2:]
s=b[::-1]
c=s+a
print(*c)
