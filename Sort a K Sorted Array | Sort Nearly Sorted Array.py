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
            a = heapq.heappop(minHeap)
            ans.append(a)
    while minHeap:
        a = heapq.heappop(minHeap)
        ans.append(a)


    return ans
