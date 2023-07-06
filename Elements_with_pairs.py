n=int(input())
l=list(map(int,input().split()))
c=[0]
if(n % 2 == 0):
    print(*l)
else:
    print(*(l+c))