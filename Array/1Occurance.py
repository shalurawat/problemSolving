A = [1,2,3,4,4,5,6,1,6,5,5]
n = 11

for i in range(n):
    count = 1
    if A[i] != -1:
        for j in range(i+1,n):
            if A[j] == A[i]:
                A[j] = -1
                count += 1
        print(f"{A[i]} occurs {count} times!")
