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
count_1 = [0 for i in range(c)]



for i in range(0,r):
    for j in range(0,c):

        if(mat[i][j]==1):
            count_1[j] += 1 

print(count_1.index(max(count_1))+1)
