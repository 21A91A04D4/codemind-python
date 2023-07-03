N= int(input())
l=len(str(N))
T=N
Sum = 0
while T > 0:
    rem = T % 10
    Sum = Sum + int(rem**l)
    T = T // 10
    l = l - 1
if Sum == N:
    print('True')
else:
    print('False')