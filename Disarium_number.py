n=int(input())
k=n
c=0
s=0
while(k > 0):
    k=k//10
    c+=1
k=n
while(k > 0):
    r=k%10
    s=s+pow(r,c)
    k=k//10
    c-=1
if(s==n):
    print("True")
else:
    print("False")