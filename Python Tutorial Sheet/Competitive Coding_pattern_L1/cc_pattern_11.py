angle = int(input())
num = int(input())
x = angle
i=0
count = 3
ans = x
while(i<num-1):

    if(i%2==0):
        ans = ans - (ans*(x**2)/((count)*(count-1))) 
    else:
        ans = ans + (ans*(x**2)/((count)*(count-1))) 

    count+=2
    
    i+=1

print(ans)
