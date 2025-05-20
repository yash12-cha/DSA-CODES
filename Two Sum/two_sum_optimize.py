def twoSum(nums, target):
    n = len(nums)
    # Store (value, original_index)
    arr = [(num, idx) for idx, num in enumerate(nums)]
    arr.sort()  # sort by value

    left = 0
    right = n - 1

    while left < right:
        total = arr[left][0] + arr[right][0]
        if total == target:
            return [arr[left][1], arr[right][1]]
        elif total > target:
            right -= 1
        else:
            left += 1

    return []  

nums = [2,7,11,15]
target = 9
ans = twoSum(nums,target)

# O(n*log(n)) time and O(1) space