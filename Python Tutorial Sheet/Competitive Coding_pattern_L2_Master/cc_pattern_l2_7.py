num = int(input())

i=1
count = 0

while(i<=num):
    if(i==1 or i==num):
        j=0
        count=0
        while(j<num):
            count+=1
            print(count,end='')
            j+=1
            

        

    else:
            
        print(" "*(num-i),end='')
        print(count,end='')
    print()

    count-=1
    i+=1
