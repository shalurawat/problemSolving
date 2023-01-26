A = [2,3,4,5,6,2,3,4,5]
n = len(A)
ans = 0
for i in range(n):
    ans = ans ^ A[i]

print(ans)
