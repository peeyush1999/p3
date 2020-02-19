r = int(input())


mat1 = []
mat2 = []
mat3 = [[0 for i in range(r)]for i in range(r)]

i=0
while(i<r):
    temp = input().split()
    mat1.append(temp)
    i+=1

for i in range(0,r):
    for j in range(0,r):
        mat1[i][j] = int(mat1[i][j])
i=0
while(i<r):
    temp = input().split()
    mat2.append(temp)
    i+=1

for i in range(0,r):
    for j in range(0,r):
        mat2[i][j] = int(mat2[i][j])

#==============================
#Assumption : Not including first and last column and row 

for i in range(r):
    for j in range(r):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

for i in mat3:
    for j in i:
        print(j,end=' ')
    print()
    
        

        
        
