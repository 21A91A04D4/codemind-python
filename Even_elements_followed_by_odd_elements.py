n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(l)):
    if(l[i] % 2 == 0):
        e.append(l[i])
    else:
        o.append(l[i])
print(*(e+o))