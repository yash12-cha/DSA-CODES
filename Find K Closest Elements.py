import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Declare empty list
        minHeap = []
        # using heapify to convert list into heap
        heapq.heapify(minHeap)
        for i in range(len(arr)):
        # Insert into Heap
        # the absolute value of the difference of x with current element
        # and the current element
            heapq.heappush(minHeap, (abs(x-arr[i]), arr[i]))
        res = []
        for j in range(k):
            diff, val = heapq.heappop(minHeap)
            res.append(val)
        res.sort()
        return res
      
'''
Time Complexity : O(n Log n)
'''
