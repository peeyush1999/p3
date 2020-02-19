mystr = input() 

prev_index = -1 
curr_index = -1 
count = 0;

i=0

while (i < len(mystr)):
    
    if(mystr[i] == ' '):
        curr_index = i

    if( curr_index - prev_index > 1):
        count = count + 1
    

    prev_index = curr_index
    i+=1


if(i - curr_index > 1):
    count+=1

print(count)
