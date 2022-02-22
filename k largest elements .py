import heapq
class Solution:

	def kLargest(self,nums, n, k):
	    # Declare empty list
        minHeap = []
        # using heapify to convert list into heap
        heapq.heapify(minHeap)
        for r in range(len(nums)):
            # adds an element into an existing heap
            heapq.heappush(minHeap, nums[r])
            if len(minHeap) > k:
                # removes the smallest element from the min heap
                heapq.heappop(minHeap)
        # sort the remaining elements in the minHeap in decreasing order
        minHeap.sort(reverse = True)
        # return minHeap
        return minHeap
