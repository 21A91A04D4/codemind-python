n=int(input())
s=n**2
l=str(s)[-len(str(n)):]
if(int(l) == n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")