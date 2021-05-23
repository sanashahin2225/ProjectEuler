#The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?
import math

def largestPrimeFactor(num):
    if isPrime(num):
        return num
    
    sqrt = int(math.sqrt(num))
    if sqrt % 2 == 0:
        sqrt += 1
    for i in range(sqrt,0,-2):
        if num % i == 0 and isPrime(i):
            return i
    # largest = 1
    # for i in range(1,int(math.sqrt(num)+1),2):
    #     if num % i == 0 and isPrime(i):
    #         largest = i
    
def isPrime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3,int(math.sqrt(num)),2):
        if num % i == 0:
            return False
    return True

print(largestPrimeFactor(600851475143))
print(largestPrimeFactor(2))
print(largestPrimeFactor(3))
print(largestPrimeFactor(5))
print(largestPrimeFactor(7))
print(largestPrimeFactor(13195))