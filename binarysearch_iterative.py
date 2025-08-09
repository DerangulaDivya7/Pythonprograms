array=[1,2,3,4,5,6,7,8,9]
x=8
def binary_iterative(array,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
result=binary_iterative(array,x,0,len(array)-1)
if result==-1:
    print("element is not found")
else:
    print(f"element is found at the index {result}")
