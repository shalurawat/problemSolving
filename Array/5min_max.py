A = [-1,0,7,3,0,-5]
N = len(A)

min = A[0]
max = A[0]

for i in range(1,N):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]

print(min + max)

