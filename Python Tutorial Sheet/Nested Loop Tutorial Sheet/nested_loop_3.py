num = int(input())
inputs = input().split(' ')
myset = set()
ans = []

count = -1
max_count =1

#assunming we can have multiple ans
for i in inputs:
    count = inputs.count(i)

    if(max_count < count):
        max_count=count    
        
    myset.add(i)

for i in sorted(myset):
    if( inputs.count(i) == max_count):
        ans.append(i)

for i in ans:
    print(i,end=' ')



