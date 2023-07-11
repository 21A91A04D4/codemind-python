n=input()
s=n.lower()
l=list(s)
c=[]
for i in l:
    if(i not in c):
        c.append(i)
c.sort()
for i in c:
    if(i == " "):
        c.remove(i)
print(len(c))