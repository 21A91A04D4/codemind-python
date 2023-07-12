n=int(input())
l=list(map(int,input().split()))
s=list(l)
s.sort(reverse = True)
if(s == l):
    print("yes")
else:
    print("no")