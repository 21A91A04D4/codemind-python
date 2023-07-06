n=int(input())
s=str(n)
l=list(s)
c=0
d=1
for i in l:
    i=int(i)
    c+=i
    d=d*i
if(c == d):
    print("Spy Number")
else:
    print("Not Spy Number")