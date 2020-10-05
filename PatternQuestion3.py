num = int(input())

i = -1*(num-1)

j = -1*(num-1)

flag = num

while(abs(i)+1<=num):

    
    j = -1*(num-1)
    while(abs(j)+1<=num):

        if(flag < abs(j)+1):
            print(flag,end='')
        else:
            print(abs(j)+1,end='')

        j+=1

    print()

    if(i<0):
        flag -=1
    else:
        flag+=1

    i+=1


            
    
