n=int(input())
s=n*n
l=str(s)
t=list(l)
c=0
for i in l:
    i=int(i)
    c+=i
if(c == n):
    print("Neon Number")
else:
    print("Not Neon Number")