n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i == 0 or i == 1):
        c=1
    else:
        c=0
if(c == 1):
    print("True")
else:
    print("False")