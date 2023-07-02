n=int(input())
s=int(input())
c=0
d=0
for i in range(1,n):
    if(n % i == 0):
        c+=i
for j in range(1,s):
    if(s % j == 0):
        d+=j
if(n==d):
    print("Amicable")
else:
    print("Not Amicable")
