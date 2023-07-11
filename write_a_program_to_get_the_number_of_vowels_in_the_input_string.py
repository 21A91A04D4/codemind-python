n=input()
l=("AEIOUaeiou")
c=0
for i in n:
    if(i in l):
        c+=1
print(c)