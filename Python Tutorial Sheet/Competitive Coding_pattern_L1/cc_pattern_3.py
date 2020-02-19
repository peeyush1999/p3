num = int(input())
count = 1
for i in range(num):
    for j in range(i+1):

        if(count%2==1):
            print("0 ",end='')
        else:
            print("1 ",end='')
        count+=1
    print()
