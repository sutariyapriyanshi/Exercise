# Tranpose Matrix

# Using for loop
B=[[1, 2],
   [4, 6],
   [7,8]]
T = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(B)):
    for j in range(len(B[0])):
        T[j][i]=B[i][j]
for t in T:
    print(t)
print(T)

# Using list comprehension
A=[[1, 5, 8],
   [9, 1, 4]]

T= [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for t in T:
    print(t)
