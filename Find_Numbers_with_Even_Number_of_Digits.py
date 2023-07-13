n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    i=str(i)
    i=list(i)
    s=len(i)
    if(s % 2 == 0):
        c.append(i)
print(len(c))