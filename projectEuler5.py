# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution():
    for num in range(2520, 999999999, 2520):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution()
    if solution is None:
        print("No answer found")
    else:
        print(f"found an answer: {solution}")