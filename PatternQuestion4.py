def myseq(x):
    if(x==1):
        return 1
    elif(x==2):
        return 1

    if(x%2==0):
        return 3**(int(x/2)-1)
    else:
        return 2**(int(x/2))
    
num = int(input())
i=1


print(myseq(num))
    

