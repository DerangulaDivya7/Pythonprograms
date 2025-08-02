
def factors(n):
    print("Factors of", n, "are:")
    for i in range(1, n + 1): # Loop from 1 to n
        if n % i == 0:
            print(i)
num = int(input("Enter a number: "))
factors(num)
