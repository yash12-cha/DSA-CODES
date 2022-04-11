import heapq
def kthLargest(nums,k):
    n = len(nums)
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
    # removes and returns the smallest element from the min heap
    return heapq.heappop(minHeap)
arr = list(map(int,input().split()))
k = int(input())
s = kthLargest(arr,k)
print(s)
        
'''
Input:-
3 2 3 1 2 4 5 5 6
4

Output:-
4

Time Complexity: - O(nlogk)
'''
