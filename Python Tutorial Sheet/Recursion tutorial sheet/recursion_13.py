def revArray(mylist,start,end):

    if(end<start):
        return mylist
    
    temp = mylist[start]
    mylist[start] = mylist[end]
    mylist[end] = temp
    
    
    return revArray(mylist,start+1,end-1)
    
     
num = int(input())
inputs = input().split(' ')

for i in range(num):
    inputs[i] = int(inputs[i])
 


print(revArray(inputs,0,len(inputs)-1))
