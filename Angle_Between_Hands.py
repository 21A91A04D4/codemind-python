a,b=map(int,input().split(":"))
s=abs(5.5*b-30*a)
if(s > 180):
    print(360-s)
else:
    print(s)