B = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
N = len(B)
A = sorted(B)
m = 7
sub = 0
minDiff = max(A)
j = m-1
for i in range(N+1-m):
    sub = A[j] - A[i]

    if minDiff > sub:
        minDiff = sub
    j += 1

print(minDiff)
