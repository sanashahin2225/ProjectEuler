# The sum of the squares of the first ten natural numbers is,
#                     (1^2 + 2^2 + 3^2 + ... 10^2) = 385
# The square of the sum of the first ten natural numbers is,
#                     (1+2+3+ ... 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#                     3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def defiiferenceSum(n):
    d = 1
    a = 1
    S = (2 * a + (n - 1) * d) * int(n/2)
    sq = int((n * (n+1)* (2 * n + 1))/6)
    return((S ** 2) - sq)


print(defiiferenceSum(100))