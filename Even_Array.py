n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i % 2 == 0):
        c+=1
if(c == len(l)):
    print("True")
else:
    print("False")