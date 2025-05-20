def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [j, i]
    return []

nums = [2,7,11,15]
target = 9
ans = twoSum(nums,target)

# O(n^2) time and O(1) space