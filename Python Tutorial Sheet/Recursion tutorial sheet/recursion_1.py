def fact(x):
    if(x == 0):
        return 1
    elif(x == 1):
        return 1

    return x*fact(x-1)

num = int(input())

print(fact(num))
