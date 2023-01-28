nums = [2,4,3,0]
target = 2

for i in range(len(nums)):
    if nums[i] < target:
        for j in range(i+1,len(nums)):
            if nums[j] <target:
                sum = nums[i] + nums[j]
                if sum == target:
                    print(i,j)
