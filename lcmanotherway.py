a=int(input("enter number"))
b=int(input("enter number"))
t1,t2=a,b
while b>0 :
    r=a%b
    a=b
    b=r
GCD=a
LCM=(t1*t2)/GCD
print(LCM)
