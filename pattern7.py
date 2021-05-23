'''
1
234
56789

'''

def pattern(rows):
    stop = 2
    cn = 1
    for i in range(rows):
        for j in range(1,stop):
            print(cn,end=" ")
            cn += 1
        print("\r")
        stop += 2

pattern(3)