'''
012345
01234
0123
012
01

'''

def pattern(n):
    for i in range(n,0,-1):
        for j in  range(0,i+1):
            print(j,end=' ')
        print("\r")

pattern(5)