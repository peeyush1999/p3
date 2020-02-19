def mult(x,y):

    
    if( y == 0):
        return 0
    if( y == 1):
        return x
    
    
    return x+mult(x,y-1)

num1 = int(input())
num2 = int(input())

temp = mult(num1,num2)

print(temp)
