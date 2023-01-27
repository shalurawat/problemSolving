B = [-2,1,-3,4,-1,2,1,-5,4]
A = [5,4,-1,7,8]
N = 5

maxSum = 0

for i in range(N):
    for j in range(i,N):
        sum = 0
        for k in range(i,j+1):
            sum = sum + A[k]
            if maxSum <= sum :
                maxSum = sum

print(maxSum)

