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
count = 0
max_count = 0


for i in range(0,r):
    count=0
    for j in range(0,c):
        if(mat[i][j] == 1):
            count+=1
        else:
            if(count > max_count):
                max_count = count
            count=0
    
print(max_count)
