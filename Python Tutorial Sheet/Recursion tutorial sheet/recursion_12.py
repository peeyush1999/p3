def sumArray(mylist,msum=0,count=0):
    
    if(count==len(mylist)):
        return msum

    msum = msum + mylist[count]
    
    return sumArray(mylist,msum,count+1)
    
     
num = int(input())
inputs = input().split(' ')

for i in range(num):
    inputs[i] = int(inputs[i])
 


print(sumArray(inputs))
