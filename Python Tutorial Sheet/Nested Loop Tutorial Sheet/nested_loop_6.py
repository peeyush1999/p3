r,c = input().split(' ')
r = int(r)
c = int(c)

mat=[]
odd = []
even = []
i=0
while(i<r):
     temp = input().split(' ')
     mat.append(temp)
     i+=1

for row in mat:
    for col in row:
        if(int(col)%2==0):
            even.append(col)
        else:
            odd.append(col)

for i in even:
    print(i,end=' ')

print()
for j in odd:
    print(j,end=' ')
