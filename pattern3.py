'''
55555
4444
333
22
1

'''

def pattern(n):
    i=n
    for k in range(n,0,-1):
        print(str(i)*k)
        i -= 1    
    print("\r")

pattern(5)