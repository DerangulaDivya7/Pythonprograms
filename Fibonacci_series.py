a=0
b=1
n=8
print("",a,"",b,end="")  
for i in range(0,n):
    c =a+b;
    a=b;
    b=c;
    print(" ",c,end="")   
    
    
