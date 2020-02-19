#take input using enter key
# num1 Enter Key
# num2

def istwinprime(x):
    
    if(x<2):
        return False
    else:
        for i in range(2,x):
            if (x%i == 0):
                return False
    return True
    


num1 = int(input())
num2 = int(input())


if(abs(num1-num2) == 2):
    if( istwinprime(num1) and istwinprime(num2)):
        print("yes")
    else:
        print("no")

else:
    print("no")

