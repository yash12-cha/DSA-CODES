def productExceptSelf(nums):
    n = len(nums)
    # Initialize a list to store the result, initially filled with 1s
    ans = [1] * n
    # Initialize a variable to store the product of all elements before the current element
    productOfAllBeforeCurrent = 1
    # Calculate the product of all elements to the left of each element
    for i in range(n):
        ans[i] = productOfAllBeforeCurrent
        productOfAllBeforeCurrent *= nums[i]
    # Initialize a variable to store the product of all elements after the current element
    productOfAllAfterCurrent = 1
    # Calculate the product of all elements to the right of each element
    for i in range(n - 1, -1, -1):
        ans[i] *= productOfAllAfterCurrent
        productOfAllAfterCurrent *= nums[i]
    # Return the final result
    return ans
nums = list(map(int, input("Input array (space-separated integers): ").split()))
ans = productExceptSelf(nums)
print("Output:", ans)
