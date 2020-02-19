num = int(input())
term1 = int(input())
term2 = int(input())
term3 = int(input())

i=1
ans = 0

while(i<=num):
    termn = term1 + (term3-term2)*(i-1)
    ans = ans + termn 
    i+=1
    print(termn," ",end='')

print()
print(ans)

    
