

mystr = input()
flag = 0
i=0
while(i<len(mystr)):
    if(mystr[i]=='.'):
        while(i<len(mystr)):        
            if(mystr[i]=='e'):
                i+=1
                if(mystr[i]=='+' or mystr[i]=='-'):
                    i+=1
                    if(mystr[i].isdigit()):
                        flag=1
                                
                    i+=1    
            i+=1

    i+=1
if(flag==0):
    print("invalid")
else:
    print("valid")
