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
max_rows=[]
max_cols=[-100000000 for i in range(c)]



for i in range(0,r):
    max_rows.append(max(mat[i]))
    for j in range(0,c):
        if(mat[i][j] >= max_cols[j]):
            max_cols[j] = mat[i][j]

for i in max_rows:
    print(i,end=' ')
print()
for i in max_cols:
    print(i,end=' ')



