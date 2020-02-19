num = int(input())
inputs = input().split(' ')
myset = set()

for i in inputs:
    myset.add(i)




for i in sorted(myset):
    print(i,":",inputs.count(i))

