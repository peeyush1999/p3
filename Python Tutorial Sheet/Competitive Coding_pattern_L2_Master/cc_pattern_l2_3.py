num = int(input())
tnum = num

count = 1
i=0

while(i<num):
    print(" "*i,end='')
    tcount = count

    j=0
    while(j<tnum):
        print(count,end='')
        print("*",end='')
        count+=1
        j+=1    

    j=0
    while(j<tnum):
        print( tnum*tnum + tcount,end='')
        if(j!= tnum-1):
            print("*",end='')
        j+=1
        tcount+=1

    print()
    tnum-=1
    i+=1
