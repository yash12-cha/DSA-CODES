import heapq
def kLargest(nums,k):
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
    # sort the remaining elements in the minHeap in decreasing order
    minHeap.sort(reverse=True)
    # return minHeap
    return minHeap
arr = list(map(int,input().split()))
k = int(input())
s = kLargest(arr,k)
print(*s)

'''
Input:-
7 10 4 3 20 15
3

Output:-
20 15 10

Time Complexity:- O(nlogk)
'''
