s=int(input())
c=0
t=abs(s)
if(s > 0):
    while(s):
        r=s % 10
        c=c*10+r
        s=s//10
    print(c)
else:
    while(t):
        r=t % 10
        c=c*10+r
        t=t//10
    print(-c)