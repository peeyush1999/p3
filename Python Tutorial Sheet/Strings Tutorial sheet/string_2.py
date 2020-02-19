str_len = int(input())
mystr = input()
count = 0

for i in mystr:
    if(i.isdigit()):
        count = count + 1


print(count)
