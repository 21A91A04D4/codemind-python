n=int(input())
rev = 0
k=n
s=n**2
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
r=rev**2
t=str(r)[::-1]
if(s == int(str(r)[::-1])):
    print("True")
else:
    print("False")