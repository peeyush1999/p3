num = int(input())
r,c = input().split()
r = int(r)
c = int(c)

inputs = input().split(' ')

ans = []


count = 0
i=0
while(i<r):
    j=0
    temp = []
    while(j<c):
        temp.append(inputs[count])
        count+=1
        j+=1

    ans.append(temp)
    i+=1

for row in ans:
    for col in row:
        print(col,end=' ')
    print()
