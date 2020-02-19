n=4
num=n-1
i=1
while(i<=n):
    j=1

    while(j<=i):
        print(num,end='')
        j+=1
    num+=1
    print()

    i+=1
    
num = num-2

i=n-1

while(i>=1):
    j=1
    
    while(j<=i):
        print(num,end='')
        j+=1
    num-=1
    print()

    i-=1
