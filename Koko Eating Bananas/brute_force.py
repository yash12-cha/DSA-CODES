import math
from typing import List
class Solution:
    def total_hours(self, speed: int, piles: List[int]) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high  # Initialize result to the maximum speed
        for speed in range(low, high + 1):
            total_hrs = self.total_hours(speed, piles)
            if total_hrs <= h:
                result = min(speed,result)
        return result
    
sol = Solution()
piles = [3,6,7,11]
h = 8
ans = sol.minEatingSpeed(piles,h)

'''
🕒 Time Complexity

-> Outer Loop: Iterates through all possible eating speeds from 1 to max(piles). Let m = max(piles). This results in O(m) iterations.
->Inner Computation: For each speed k, the total_hours function computes the total hours needed by iterating over all n piles, leading to O(n) operations per iteration.
-> Overall Time Complexity: Combining both, the total time complexity is O(n * m).
This can be inefficient, especially when max(piles) is large.

🧠 Space Complexity

-> Auxiliary Space: The algorithm uses a constant amount of extra space for variables like low, high, result, and loop counters.
-> Overall Space Complexity: O(1) (excluding the input list piles).
'''