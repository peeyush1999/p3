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
    

for i in range(0,r):
    for j in range(0,c):

        if(i>j):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    
for i in mat:
    for j in i:
        print(j," ",end='')
    print()
    
