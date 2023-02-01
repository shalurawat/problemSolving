nums = [1,2,3,4,5,6,7]
nums = [1,2,3,1]
N = len(nums)

def duplicate(nums, N):
    for i in range (N):
        for j in range(i+1,N):
            if nums[i] == nums[j]:
                return True
    
    return False

X = duplicate(nums,N)
print(X)

