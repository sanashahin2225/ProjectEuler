# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def nthPrime(num):
    count = [2]
    number = 3
    while len(count) < num:
        if isPrime(number):
            count.append(number)
        
        number += 2

    return count[-1]   

def isPrime(num):
    strr = str(num)

    for i in range(3,int(math.sqrt(num))+1,2):
        if strr[-1] == 0 and strr[-1] == 2 and strr[-1] == 4 and strr[-1] == 6 and strr[-1] == 8:
            return False
        elif (sum(list(map(int, strr.strip())))) % 3 == 0:
            return False
        elif strr[-1] == 5:
            return False
        elif num % i == 0:
            return False
    return True

print(nthPrime(6))
print(nthPrime(10))
print(nthPrime(100))
print(nthPrime(1000))
print(nthPrime(10001))