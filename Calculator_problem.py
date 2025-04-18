n=int(input(" "))
n2=int(input(" "))
oper=input(" ")
if oper=='+':
    print(n+n2)
elif oper ==  '-':
    print(n-n2)
elif oper ==  '*':
    print(n*n2)
elif oper ==  '/':
    print(n/n2)
elif oper ==  '//':
    print(n//n2)
else:
    print("invalid operator")
