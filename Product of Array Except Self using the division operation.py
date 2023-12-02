def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n
    product = 1
    zero_count = 0

    for i in range(n):
        if nums[i] != 0:
            product *= nums[i]
        else:
            zero_count += 1

    for i in range(n):
        if zero_count == 0:
            ans[i] = product // nums[i]
        elif zero_count == 1 and nums[i] == 0:
            ans[i] = product
        else:
            ans[i] = 0

    return ans

nums = list(map(int, input("Input array (space-separated integers): ").split()))
ans = productExceptSelf(nums)
print("Output:", ans)
