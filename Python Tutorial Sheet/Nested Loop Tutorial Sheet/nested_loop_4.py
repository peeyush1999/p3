num = int(input())
k = int(input())
inputs = input().split(' ')
myset = set()
ans = []

count = -1
max_count =1

#assunming we can have multiple ans
for i in inputs:
    count = inputs.count(i)

    if(k == count):        
        myset.add(i)

for i in sorted(myset):
    print(i,end=' ')



