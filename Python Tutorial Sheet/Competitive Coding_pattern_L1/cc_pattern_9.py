num = int(input())
i=0
#printing upper part
while (i<num):
    j=-1*(num-1)

    while( abs(j)<=num ):

        if(abs(j)==i):
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print()
    i+=1
#printing lower part
i=i-2
while (i>=0):
    j=-1*(num-1)

    while( abs(j)<=num ):

        if(abs(j)==i):
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print()
    i-=1
