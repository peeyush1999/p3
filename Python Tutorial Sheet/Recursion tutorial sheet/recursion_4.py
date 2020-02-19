def exp(x,y):

    
    if( y == 0):
        return 1
    if( y == 1):
        return x
    
    
    return x*exp(x,y-1)

num1 = int(input())
num2 = int(input())

temp = exp(num1,num2)

print(temp)
