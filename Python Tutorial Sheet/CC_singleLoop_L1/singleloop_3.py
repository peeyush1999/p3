num = int(input())
ans =0
myexp = 1
while(num>0):
   temp = num%10
   
   ans = ans + temp*myexp
   myexp = myexp*2
   num = int(num/10)

print(ans)

