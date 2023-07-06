n=int(input())
n=str(n)
l=list(n)
s=1
c=0
for i in l:
    i=int(i)
    s=s*i
    c+=i
print(s-c)