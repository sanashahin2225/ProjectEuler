'''
1
22
333
4444
55555

'''
def pattern(num):
    for i in range(num):
        for j in range(i):
            print(i, end=" ")
        print("\r")

pattern(5)