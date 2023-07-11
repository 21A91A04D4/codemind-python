n=input().split()
c=[]
s=("AEIOUaeiou")
d=0
for i in n:
    d=0
    for j in i:
        if(j  in s):
            d+=1
    c.append(d)
print(*c)