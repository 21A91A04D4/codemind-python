s=int(input())
t=s
c=0
while(s > 0):
    r=s%10
    c=c*10+r
    s=s//10
if(t==c):
    print("True")
else:
    print("False")
