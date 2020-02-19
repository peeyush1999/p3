def sod(x,y=0):

    
    if( x == 0):
        return y
    y = y + x%10
    x = int(x/10)
    
    return sod(x,y)

num1 = int(input())


temp = sod(num1)

print(temp)
