def maxArray(mylist,max_elem=0,count=0):
    
    if(count==len(mylist)):
        return max_elem

    if(max_elem < mylist[count]):
        max_elem = mylist[count]
    
    return maxArray(mylist,max_elem,count+1)
    
     
num = int(input())
inputs = input().split(' ')

for i in range(num):
    inputs[i] = int(inputs[i])
 


print(maxArray(inputs))
