import heapq
def kthSmallest(nums,k):
    n = len(nums)
    # Declare empty list
    maxHeap = []
    # using heapify to convert list into heap
    heapq.heapify(maxHeap)
    for r in range(n):
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
arr = list(map(int,input().split()))
k = int(input())
s = kthSmallest(arr,k)
print(s)


'''
Input: -
2 1 4 3 2
3

Output:-
2

Time Complexity: - O(nlogk)
'''
