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
max_sum = -1
min_sum = 10000
min_index=0
max_index=0
for i in range(r):
    count = c-1 
    s = 0
    for j in range(c):
        s = s + mat[i][j]*(2**count)
        count-=1
    
    if(s > max_sum):
        
        max_sum = s
        max_index= i
        
    if(s < min_sum):
        min_sum = s
        min_index = i

print(min_index)
print(max_index)
        
        
