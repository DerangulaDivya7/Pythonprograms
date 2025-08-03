a=int(input("enter number"))
b=int(input("enter number"))
small=min(a,b)
for i in range(1,small+1):
    if(a%i ==0 and b%i==0):
        gcd=i
print('gcd',gcd)
