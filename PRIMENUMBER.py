l=int(input("enter lower number"))
h=int(input("enter higher number"))
for i in range(l,h+1):
    count=0
    for j in range(2,i):
        if i%j ==0:
            count=count+1
    if count==0:
        print(i,end=" ")
