n=int(input())
for i in range(n):
    s=int(input())
    fact = 1
    if s == 0 or s == 1:
        print("1")
    else:
        for i in range(1, s + 1):
            fact = fact * i
        print(fact)