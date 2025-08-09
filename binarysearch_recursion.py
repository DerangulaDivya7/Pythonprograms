array=[1,30,90,4,5,67,97]
x=5
def binary_search(array,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            return binary_search(array,x,mid+1,high)
        else:
            return binary_search(array,x,low,mid-1)
result=binary_search(array,x,0,len(array)-1)
if result==-1:
    print("element is not found")
else:
    print(f"element is  found at index of {result}")
