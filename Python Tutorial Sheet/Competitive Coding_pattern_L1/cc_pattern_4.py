num = int(input())
count = 0
for i in range(num):

    if(i%2==1):
        count+=(i+1)


    for j in range(i+1):

        if(i%2==1):
            print(count-j," ",end='')
        else:
            count+=1
            print(count," ",end='')
            

        
    print()
