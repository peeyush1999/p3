

mystr = input()

count = 0
max_count = -1
max_occr=''

ans = list()#if we have multiple answer 

for i in mystr:
    count = mystr.count(i)

    if(count > max_count):
        max_count = count
        max_occr = i


for i in mystr:
    count = mystr.count(i)
    if(count == max_count):

        if(i not in ans):
            ans.append(i)
    

for i in ans:
    print(i," ",end='')
