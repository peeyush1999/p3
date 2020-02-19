def rev(x,y=0):

    
    if( x == 0):
        return y
    y = y*10 + x%10
    x = int(x/10)
    
    return rev(x,y)

num1 = int(input())


temp = rev(num1)

print(temp)
