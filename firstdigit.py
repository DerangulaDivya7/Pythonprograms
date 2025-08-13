def firstdigit(n):
    while n>=10:
        n=n//10
    return n
n=int(input())
print(firstdigit(n))
