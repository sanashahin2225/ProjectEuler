'''
1
3 2
6 5 4
10 9 8 7
'''

def pattern(num):
    for i in range(num+1):
        for j in range(i):
            print(j,end=" ")
        print("\r")

pattern(4)