'''
1
21
321
4321

'''

def pattern(n):
    for i in range(1,n):
        for j in range(i,0,-1):
            print(j, end=' ')
        print("\r")

pattern(5)