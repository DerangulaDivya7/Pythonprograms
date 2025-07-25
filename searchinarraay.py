a=([1,23,5,6])
found=False
x=23
for i in a:
    if i == x:
        found=True
        break
if found:
 print("found")
else:
    print("not found")
