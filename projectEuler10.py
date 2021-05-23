# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math

def sumOfPrimes(num):
    sumprime = 2
    for i in range(3,num,2):
        if isPrime(i):
            sumprime = sumprime + i
    
    return sumprime

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

print(sumOfPrimes(10))