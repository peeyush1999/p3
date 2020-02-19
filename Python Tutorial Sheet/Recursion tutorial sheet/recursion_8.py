def gcd(a,b):

    
    if(a == 0):
        return b
    
        

    return gcd(b%a,a)

     

num1 = int(input())
num2 = int(input())

print(gcd(num1,num2))
