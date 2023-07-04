n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if(l.count(i) == 2):
        s.append(i)
        break
print(*s)