from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_count = 0
        for num1 in arr1:
            is_valid = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_valid = False
                    break
            if is_valid:
                distance_count += 1
        return distance_count


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
sol = Solution()
distance_value = sol.findTheDistanceValue(arr1, arr2, d)

'''
Time Complexity:
-> Let n=len(arr1) and 𝑚=len(arr2)
-> For each element in arr1, we iterate through all elements in arr2 to check the condition.
-> Therefore, the time complexity is 𝑂(𝑛×𝑚)

Space Complexity:
-> We use a constant amount of extra space for variables like distance_count and is_valid.
-> Hence, the space complexity is 𝑂(1)
'''
