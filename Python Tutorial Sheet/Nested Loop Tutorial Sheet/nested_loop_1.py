num = int(input())
k = int(input())
i=0
inputs = input().split(' ')
flag = 1

for i in range(len(inputs)):
    inputs[i] = int(inputs[i])


for i in inputs:
    if(k-i in inputs):
        flag=1
        break

    else:
        flag=0

if(flag==0):
    print('no')
else:
    print('yes')



