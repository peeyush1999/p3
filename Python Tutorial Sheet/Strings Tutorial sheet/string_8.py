
mystr = input()

i=0

sub_len = 0
max_len = -1

while(i<len(mystr)):
    if(mystr[i].isdigit()):

        j=i
        sub_len=0
        
        while(j<len(mystr) and mystr[j].isdigit()):
            sub_len+=1
            j+=1
            

    if(sub_len > max_len):
        max_len = sub_len

    i+=1

    
print(max_len)

        

    
