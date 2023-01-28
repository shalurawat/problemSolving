A = [-2,1,-3,4,-1,2,1,-5,4]
B = [5,4,-1,7,8]
N = 9

maxSum = 0

for i in range(N):
    sum = 0
    for j in range(i,N):
            sum = sum + A[j]
            if maxSum <= sum :
                maxSum = sum

print(maxSum)

