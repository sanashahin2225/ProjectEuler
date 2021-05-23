def find_missing(lst,n):
    actual_sum = sum(lst)
    required_sum = n*(n+1)//2
    missing_no = required_sum - actual_sum
    return missing_no

missing = find_missing([1,2,3,5,6],6)
print(missing)