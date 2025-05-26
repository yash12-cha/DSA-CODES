import math
from typing import List
class Solution:
    def total_hours(self, speed: int, piles: List[int]) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high
        while low <= high:
            mid = (low + high) // 2
            hours = self.total_hours(mid, piles)
            if hours > h:
                # Need to eat faster
                low = mid + 1
            else:  # This includes the case where hours <= h
                result = mid  # Update result to the current mid
                high = mid - 1  # Try to find a slower speed
        return result
    
sol = Solution()
piles = [3,6,7,11]
h = 8
ans = sol.minEatingSpeed(piles,h)

'''
🕒 Time Complexity

-> Binary Search Iterations: The binary search operates over the range of possible eating speeds, from 1 to max(piles). This results in O(log m) iterations, where m = max(piles).
-> Total Hours Calculation: For each candidate speed mid, the total_hours function computes the total hours needed by iterating over all n piles, leading to O(n) operations per iteration.
-> Overall Time Complexity: Combining both, the total time complexity is O(n * log m).
This is efficient and suitable for large datasets.

🧠 Space Complexity
-> Auxiliary Space: The algorithm uses a constant amount of extra space for variables like low, high, mid, and result.
-> Overall Space Complexity: O(1) (excluding the input list piles).
'''