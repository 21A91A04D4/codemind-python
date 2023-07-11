n=input().split()
c=0
for i in n:
    a=i.lower()
    b=a[::-1]
    if(a == b):
        c+=1
print(c)