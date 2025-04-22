n=int(input("enter n value"))
matrix=[]
for i in range(n):
   s=list(map(int,input().split()))
   matrix.append(s)

  
for i in range(3):
      for j in range(3):
           a=matrix[i][j];
           print(a)
