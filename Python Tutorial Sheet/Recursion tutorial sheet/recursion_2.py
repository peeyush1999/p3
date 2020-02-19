def palindrome(x,y=0):

    if( x == 0):
        return y

    rem = x%10
    y = y*10 + rem  
    x = int(x/10)
    return palindrome(x,y)

num = int(input())
temp = palindrome(num,0)

if( num == temp):
    print("Palindrome")
else:
    print("Not Palindrome")
