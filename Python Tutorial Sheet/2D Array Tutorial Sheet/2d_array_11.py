r,c = input().split(' ')
r = int(r)
c = int(c)

k = int(input())

mat1 = []

i=0
while(i<r):
    temp = input().split()
    mat1.append(temp)
    i+=1

for i in range(0,r):
    for j in range(0,c):
        mat1[i][j] = int(mat1[i][j])



i=0
col=0
row=r
#getting starting index of diagonal
while(i<k):
    if(row==0):
        col+=1
    else:
        row-=1
    i+=1
    
        
i=0
j=0
while(row<r):
    while(col<c):
        if(row>=r):
            break
        print(mat1[row][col],end=' ')
        
        row+=1
        col+=1

        
        
        
