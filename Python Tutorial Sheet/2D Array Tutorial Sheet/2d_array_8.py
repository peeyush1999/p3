r,c = input().split(' ')
r = int(r)
c = int(c)

mat = []

i=0
while(i<r):
    temp = input().split()
    mat.append(temp)
    i+=1

for i in range(0,r):
    for j in range(0,c):
        mat[i][j] = int(mat[i][j])

#==============================
#Assumption : Not including first and last column and row 

for i in range(1,r-1):
    for j in range(1,c-1):
        if( (mat[i][j] > mat[i][j+1]) and (mat[i][j] > mat[i][j-1])):
             if( (mat[i][j] > mat[i+1][j]) and (mat[i][j] > mat[i-1][j])):           
                print(mat[i][j])

        
        
