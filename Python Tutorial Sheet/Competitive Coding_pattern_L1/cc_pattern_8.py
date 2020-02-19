num = int(input())
i=0
while (i<num):
    j=-1*(num-1)
    while( abs(j)<=num ):

        if(abs(j)<=i):
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print("")
    i+=1
