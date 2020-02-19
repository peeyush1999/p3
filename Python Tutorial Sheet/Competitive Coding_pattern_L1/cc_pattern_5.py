num = int(input())
count = 0
for i in range(num):
    count+=(i+1)
    for j in range(i+1):
        print(count-j," ",end='')
    print()
