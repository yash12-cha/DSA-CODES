def twoSum(nums, target):
    num_indicies = {}
    for idx, ele in enumerate(nums):
        complement = target - ele

        if complement in num_indicies:
            return [num_indicies[complement], idx]
        num_indicies[ele] = idx
    return []

nums = [2,7,11,15]
target = 9
ans = twoSum(nums,target)

# O(n) time and O(n) space