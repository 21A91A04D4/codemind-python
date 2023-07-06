n=int(input())
l=list(map(int,input().split()))
a=l[:len(l)//2]
b=l[len(l)//2:]
print(sum(a))
print(sum(b))