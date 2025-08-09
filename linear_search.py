array=[1,3,4,5,6,7,8,9]
x=9
n=len(array)
def linear(array,n,x):
    for i in range(0,n):
      if array[i]==x:
         return i
    return -1
result=linear(array,n,x)
if result==-1:
   print("element is not found")
else:
   print(f"element is found at index:{result}")
   
