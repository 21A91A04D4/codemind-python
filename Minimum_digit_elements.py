n=int(input())
l=input().split()
c=[]
for i in l:
    s=len(i)
    c.append(s)
print(c.count(min(c)))