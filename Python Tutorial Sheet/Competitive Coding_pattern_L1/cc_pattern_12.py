def myseq(x):
    a = 2
    b = 10
    i = 1
    ans = 0
    while(i<=x):
        ans =ans + (a + b)
        a*=3
        b*=2
        i+=1
    return ans
    
num = int(input())

print(myseq(num))


    
