A=[[1, 5, 8],
   [9, 1, 4],
   [3, 6, 9]]
B=[[4, 9, 5],
   [5, 6, 2],
   [2, 7, 5]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

print("The Given matrix is as below")
print("Matrix A ")
for a in A:
    print(a)
print("\nMatrix B ")
for b in B:
    print(b)
print("\nResultant Matrix")
for i in range(len(A)): # for performing iteration in rows
    for j in range(len(A[0])): # for columns
        result[i][j]=A[i][j]+B[i][j]

for r in result:
    print(r)
