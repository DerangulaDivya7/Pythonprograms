a=int(input("enter number"))
b=int(input("enter number"))
while b!=0:
    r=a%b
    a=b
    b=r
print(a)
