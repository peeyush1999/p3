def dec2bin(num,count=0):
    if(num==0):
        return 0
    return num%2*10**count + dec2bin(int(num/2),count+1)
     

num = int(input())


print(dec2bin(num))
