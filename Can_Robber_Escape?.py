n=int(input())

l=list(map(int,input().split()))

odd,even=0,0

for i in l:

    if i%2!=0:

        odd+=1

if odd>2:

    print('NO')

else:

    print("YES")