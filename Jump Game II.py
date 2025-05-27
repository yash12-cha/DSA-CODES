from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l = r = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
        return jumps
nums = [2,3,1,1,4]
sol = Solution()

min_jumps = sol.jump(nums)

'''
✅ Time Complexity: O(n)
-> The function uses a greedy approach to determine if the end of the array is reachable.
-> In each iteration of the while loop, it processes a window of indices from l to r.
-> Across all iterations, each index is visited at most once.
-> Therefore, the total number of operations is proportional to the length of the array.
-> The time complexity is linear with respect to the size of the input array.

✅ Space Complexity: O(1)
-> The function utilizes a constant number of variables (n, l, r, farthest) regardless of the input size.
-> No additional data structures (like arrays or hash maps) are used that scale with the input.
-> The space complexity remains constant, irrespective of the input array's size.
'''