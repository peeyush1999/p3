def findfact(x):
    if(x==0 or x==1):
        return 1;

    return x*findfact(x-1)


num = int(input())
ans =0
while(num>0):
   temp = num%10
  
   ans = ans + findfact(temp)
   num = int(num/10)

print(ans)

