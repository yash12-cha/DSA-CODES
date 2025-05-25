def nextPermutation(nums):
    """
    Modify nums in-place to the next lexicographical permutation.
    """
    n = len(nums)
    idx = -1
    # Step 1: Find the first decreasing element from the end
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            idx = i
            break
    if idx == -1:
        # The entire array is in descending order
        nums.reverse()
        return
    # Step 2: Find the element just larger than nums[idx] to the right
    for i in range(n - 1, idx, -1):
        if nums[i] > nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
            break
    # Step 3: Reverse the sublist after idx
    nums[idx + 1:] = reversed(nums[idx + 1:])
    return nums


nums = [1,2,3]
ans = nextPermutation(nums)

'''
Time complexity:

-> Identifying the Pivot:
- Traverses the list from the end to find the first pair where nums[i] < nums[i + 1].
- In the worst case, this requires scanning the entire list, resulting in O(n) time.

-> Finding the Successor and Swapping:
- Again traverses from the end to find the first element greater than the pivot and swaps them.
- This step also takes O(n) time in the worst case.

-> Reversing the Suffix:
- Reverses the sublist after the pivot index.
- This operation is O(n) in the worst case.

Since these steps are executed sequentially and each is O(n), the overall time complexity remains O(n).

Space complexity:
The function modifies the input list in-place and uses a constant amount of additional space for variables like indices and temporary storage during swapping. Therefore, the space complexity is O(1).
'''