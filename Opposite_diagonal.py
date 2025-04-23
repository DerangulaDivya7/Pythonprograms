n=int(input("enter n value"))
matrix=[]
for i in range(n):
   s=list(map(int,input().split()))
   matrix.append(s)
z=n-1
for i in range(n):
           a=matrix[i][z-i];
           print(a)
