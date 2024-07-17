# Python Code to search in a rotated sorted array

def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_min_index(nums):
    n = len(nums)
    left, right = 0, n - 1
    if nums[left] < nums[right]:
        return 0
    while left <= right:
        mid = left + (right - left) // 2
        next_idx = (mid + 1) % n
        prev_idx = (mid + n - 1) % n
        if nums[mid] <= nums[next_idx] and nums[mid] <= nums[prev_idx]:
            return mid
        if nums[mid] <= nums[right]:
            right = mid - 1
        elif nums[left] <= nums[mid]:
            left = mid + 1
    return -1

def search(nums, target):
    n = len(nums)
    min_index = find_min_index(nums)
    result1 = binary_search(nums, target, 0, min_index - 1)
    result2 = binary_search(nums, target, min_index, n - 1)
    if result1 == -1:
        return result2
    else:
        return result1
