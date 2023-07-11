n=input().split()
s=("AEIOUaeiou")
c=0
for i in n:
    l=list(i)
    if(l[0] in s and l[len(l)-1] not in s):
        c+=1
print(c)