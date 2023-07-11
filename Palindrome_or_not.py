s=input().split()
c=0
for i in s:
    a=i.lower()
    l=a[::-1]
    if(a == l):
        c+=1
if(c == 1):
    print("True")
else:
    print("False")