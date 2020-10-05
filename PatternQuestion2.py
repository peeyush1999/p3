num = int(input())

i=1
count = 0

while(i<=num):

    if(i==1 or i==num):
        print(i,end='')
        print(" "*(num-2),end='')
        print(i,end='')

        print()
    else:
        print(i,end='')
        print(" "*(count),end='')
        print(i,end='')
        print(" "*((num-3)-count),end='')
        print(i,end='')
        count+=1
        print()

    i+=1
