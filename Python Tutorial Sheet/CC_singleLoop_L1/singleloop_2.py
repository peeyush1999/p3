
num = int(input())
ans =0
while(num>0):
   temp = num%10
   
   ans = ans + temp
   num = int(num/10)

print(ans)

