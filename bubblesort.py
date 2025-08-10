data=[1,5,6,7,8,9,3,2,4]
def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
print("list before sorting",data)
k=bubblesort(data)
print(k)
