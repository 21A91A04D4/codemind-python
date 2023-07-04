n=int(input())
l=list(map(int,input().split()))
s=sum(l)
while n:
    if(s % n == 0):
        print(n)
        break
    n=n-1