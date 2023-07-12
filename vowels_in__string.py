s=input()
l=("AEIOUaeiou")
c=[]
d=[]
for i in s:
    if(i in l):
        c.append(i)
for i in c:
    if(i not in d):
        d.append(i)
print(*d)