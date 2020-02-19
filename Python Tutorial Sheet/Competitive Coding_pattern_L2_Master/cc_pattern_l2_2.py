row = int(input())
cols = int(input())
i=0
while(i<row):
    if(i==0 or i==row-1):
        print(" "*i+"*"*cols)
    else:
        print(" "*i + "*" +" "*(cols-2)+ "*")
    i+=1

