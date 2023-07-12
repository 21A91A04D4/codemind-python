s=input()
l=("aqzswxedcrfvtgbyhnujmikolpAQZWSXEDCRFVTGBYHNUJMIKOLP1234567890 ")
c=0
for i in s:
    if(i not in l):
        c+=1
print(c)