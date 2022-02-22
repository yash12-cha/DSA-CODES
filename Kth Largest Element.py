import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        # Declare empty list
        minHeap = []
        # using heapify to convert list into heap
        heapq.heapify(minHeap)
        for r in range(len(nums)):
            # adds an element into an existing heap
            heappush(minHeap, nums[r])
            if len(minHeap) > k:
                # removes the smallest element from the min heap
                heappop(minHeap)
        # removes and returns the smallest element from the min heap
        return heappop(minHeap)
        
        
