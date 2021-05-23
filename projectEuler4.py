# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers. 100-999



def largestPalindromeProduuct(num):
    number = int('9' * num)
    largest = 1
    for i in range(number,0,-1):
        for j in range(number,0,-1):
            mult = i * j
            if isPalindrome(mult) and largest < mult:
                largest = mult
    
    return largest


def isPalindrome(num):
    temp = str(num)
    if temp == temp[::-1]:
        return True
    else:
        return False

print(largestPalindromeProduuct(3))
