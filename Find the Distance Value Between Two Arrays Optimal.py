from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        arr2.sort()
        for i in range(len(arr1)):
            left,right=0,len(arr2)-1
            while left<=right:
                mid=(left+right)//2
                if abs(arr1[i]-arr2[mid])<=d:
                    count+=1
                    break
                elif arr1[i]<arr2[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return len(arr1)-count


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
sol = Solution()
distance_value = sol.findTheDistanceValue(arr1, arr2, d)

'''
Time Complexity:
-> Sorting arr2 takes O(mlogm).
-> For each element in arr1, we perform a binary search on arr2, which takes O(logm).
-> Therefore, the total time complexity is O(mlogm+nlogm).

Space Complexity:
-> Sorting arr2 may require O(m) space, depending on the sorting algorithm used.
-> Apart from that, we use a constant amount of extra space.
-> Hence, the space complexity is O(m) in the worst case.
'''
