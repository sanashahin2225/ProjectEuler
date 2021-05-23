def is_palindrome(S):
    if S == S[::-1]:
        return True
    else:
        return False

print("Yes") if is_palindrome("AADAA") else print("No")