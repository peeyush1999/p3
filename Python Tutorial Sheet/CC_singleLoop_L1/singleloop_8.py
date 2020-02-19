
def isprime(x):
    
    if(x<2):
        return False
    else:
        for i in range(2,x):
            if (x%i == 0):
                return False
    return True
    


num1 = int(input())


i=2;
flag=0;
while i<num1:

    if(isprime(i)):
        
        if(num1%i == 0 and isprime(int(num1/i))):
            flag=1
            break;
        else:
            flag=0
    else:
        flag=0

    i+=1

if(flag==0):
    print("no")
else:
    print("yes")
