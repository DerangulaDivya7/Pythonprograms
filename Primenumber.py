def is_prime(number):
    if number>1:
        for n in range(2,number):
            if number%n == 0:
                return "not prime numbers"
        return   "prime number"
    return "not prime"
t =int(input())   
print(is_prime(t))          
