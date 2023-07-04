n=int(input())
c=0
k=0
for i in range(1,n+1):
    c=0
    if(n % i == 0):
        for j in range(1,i+1):
            if(i % j == 0):
                c+=1
        if(c != 2):
            k+=1
print(k)