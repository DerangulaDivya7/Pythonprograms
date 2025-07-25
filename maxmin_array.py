a=([1,2,3,4])
min_num=a[0]
max_num=a[0]
for num in a:
    if num>max_num:
       max_num=num
    elif num<min_num:
        min_num=num
print(max_num)
print(min_num)
