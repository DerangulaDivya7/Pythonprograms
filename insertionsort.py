data=[2,1,2,8,9,6,5]
def insertionsort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
print("before sorting",data)
insertionsort(data)
print("after sorting",data)
