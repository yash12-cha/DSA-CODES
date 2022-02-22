import heapq
class Solution:
    def kthSmallest(self,nums, l, r, k):
        # Declare empty list
        maxHeap = []
        # using heapify to convert list into heap
        heapq.heapify(maxHeap)
        for r in range(len(nums)):
            # Adding items to the heap using heappush
            # function by multiplying them with -1
            heapq.heappush(maxHeap, -1 * nums[r])
            if len(maxHeap) > k:
                # removes the smallest element from the max heap
                heapq.heappop(maxHeap)
        # removes and returns the smallest element from the max heap
        c = heapq.heappop(maxHeap)
        # multiplying with -1
        return -1 * c
'''
Time Complexity: - O(nlogk)
'''
