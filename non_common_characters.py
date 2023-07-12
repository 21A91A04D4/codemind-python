a=input()
b=input()
c=a.lower()
d=b.lower()
s=[]
for i in c:
    if(i not in d and i not in s and i != " "):
        s.append(i)
for i in d:
    if(i not in c and i not in s and i != " "):
        s.append(i)
s.sort()
print("".join(s))