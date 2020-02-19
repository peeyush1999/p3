num = int(input())
count = 1
for i in range(num):
    for j in range(i+1):

        if((j%2==0 and i%2==1) or (j%2==1 and i%2==0)):
            print("-"+str(count)," ",end='')
        else:
            print(count," ",end='')
        count+=1
    print()

