n=int(input())
c=0
for i in range(1,n):
    if(i*i == n):
        c+=1
if(c == 1):
    print("True")
else:
    print("False")