a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i < 0):
        i=-i
    i=str(i)
    s=len(i)
    if(b == s):
        c+=1
print(c)