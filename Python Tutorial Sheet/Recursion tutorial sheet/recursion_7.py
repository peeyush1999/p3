def fib(x):

    
    if(x == 0):
        return 0
    if(x == 1):
        return 1

    return (fib(x-1) + fib(x-2))    

     

num1 = int(input())

print(fib(num1-1))
