num = int(input())

count = 1
i=1
while(i<=(num)):
    if(i != num):
        print(count,end='')
        print(" "*(num-2),end='')
        print(num+1-count)
        count+=1
    else:
        j=num
        while(j>=1):
            print(j,end='')
            j-=1
    
    i+=1

print()
i=1
count = 1
while(i<=(num-1)):
        print(num-count,end='')
        print(" "*(num-2),end='')
        print(count+1,end='')
        count+=1
        print()
        i+=1


            
