
length = int(input())
mystr = input()

flag = 0
i=0

while(i < length/2):
    if(mystr[i] == mystr[length-1-i]):
        flag = 1
        

    else:
        flag = 0
        break
    
    i+=1

if(flag==1):
    print('Palindrome')
else:
    print('Not Palindrome')
