n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i % 2 == 0):
        c+=i
    else:
        break
print(c)