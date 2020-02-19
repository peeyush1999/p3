num = int(input())
count = 1
for i in range(num):
    for j in range(i+1):

        if(i%2==1):
            print("-"+str(count)," ",end='')
        else:
            
            print(count," ",end='')
        count+=1

        
    print()
