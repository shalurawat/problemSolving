#m elements exists twice

A = [1,2,3,2,1,3,4,5,6,5,6]
n = len(A)

for i in range(n):
    if A[i] != -1 :
        for j in range(i+1,n):
            if A[j] == A[i]:
                A[j] = -1
                A[i] = -1

for i in range(n):
    if A[i] != -1:
        print(f"The unique element present in Array is : {A[i]}")