#chr(<val>) : converts ASCII value corresponding to ch.

def myseq(x):
    a = 65
    b = 90
    i = 1
    
    while(i<=x):
        print(chr(a)+chr(b)," ",end='')
        a+=2
        b-=1
        i+=1
    
    
num = int(input())

myseq(num)


    
