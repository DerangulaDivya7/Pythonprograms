x=[[12,9,3],
[4,5,6],
[7,8,3]]
y=[[9,8,1],
[6,7,3],
[4,5,9]]
result=[[0,0,0],
[0,0,0],
[0,0,0]]  
for i in range (len(x)):
     for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for t in result:
    print(t)       
   
