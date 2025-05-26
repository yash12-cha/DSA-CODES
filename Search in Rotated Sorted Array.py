from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            # Left Sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right Sorted
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
                
nums = [4,5,6,7,0,1,2]
target = 0
sol = Solution()
ans = sol.search(nums, target)

'''
🕒 Time Complexity

-> Binary Search Iterations: In each iteration, the algorithm halves the search space by comparing the target with the middle element and determining which half is properly sorted. This results in a logarithmic number of iterations.
-> Overall Time Complexity: O(log n), where n is the number of elements in the array.
This efficiency stems from the binary search mechanism, which consistently reduces the search interval by half.

🧠 Space Complexity
-> Auxiliary Space: The algorithm uses a constant amount of extra space for variables like low, high, and mid.
-> Overall Space Complexity: O(1) The search is conducted in place without utilizing additional data structures.
'''