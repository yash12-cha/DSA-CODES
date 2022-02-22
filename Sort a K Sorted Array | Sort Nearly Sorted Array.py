import heapq
def nearlySorted(nums, k):
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    ans = []
    for r in range(len(nums)):
        # adds an element into an existing heap
        heapq.heappush(minHeap, nums[r])
        if len(minHeap) > k:
            # removes the smallest element from the min heap
            a = heapq.heappop(minHeap)
            # add the removed element into the answer list
            ans.append(a)
    # pop all remaining elements from the min-heap and assign them to the answer list
    while minHeap:
        a = heapq.heappop(minHeap)
        ans.append(a)


    return ans
