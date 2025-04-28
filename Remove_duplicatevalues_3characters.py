s='AABCAAADA'
k=3
start=0
end=k
while end<=len(s):
    temp=s[start:end]
    a=list(set(list(temp)))
    print("".join(a))
    start +=k
    end += k
