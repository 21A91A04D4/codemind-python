n=int(input())
c=0
while(n > 9):
    c=0
    while(n):
        a=n % 10
        c=c+a*a
        n=n // 10
    n=c
if(c == 1):
    print("True")
else:
    print("False")