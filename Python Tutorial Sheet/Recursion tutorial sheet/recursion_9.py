def bin2dec(num,count=0):

    if(num==0):
        return 0

    return (num%10)*2**count + bin2dec(int(num/10),count+1)
    
    
    
    
     

num = int(input())


print(bin2dec(num))
