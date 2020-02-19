r,c = input().split(' ')
r = int(r)
c = int(c)

r1,c1 = input().split(' ')
r1 = int(r1)
c1 = int(c1)

mat1 = []
mat2 = []
mat3 = [[0 for i in range(r)]for i in range(r)]

i=0
while(i<r):
    temp = input().split()
    mat1.append(temp)
    i+=1

for i in range(0,r):
    for j in range(0,c):
        mat1[i][j] = int(mat1[i][j])
i=0



while(i<r1):
    temp = input().split()
    mat2.append(temp)
    i+=1

for i in range(0,r1):
    for j in range(0,c1):
        mat2[i][j] = int(mat2[i][j])

#==============================
#Assumption : Not including first and last column and row 

for i in range(r):
    for j in range(r):
        for k in range(r):
            mat3[i][j] = mat3[i][j] + mat1[i][k]*mat2[k][j]

for i in mat3:
    for j in i:
        print(j,end=' ')
    print()
    
        

        
        
