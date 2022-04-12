import heapq
def kSorted(nums,k):
    n = len(nums)
    # List to store answer
    ans = []
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for r in range(len(nums)):
        # adds an element into an existing heap
        heapq.heappush(minHeap, nums[r])
        if len(minHeap) > k:
            # removes the smallest element from the min heap
            ans.append(heapq.heappop(minHeap))
    # pop all remaining elements from the min-heap and store in the answer list
    while minHeap:
        ans.append(heapq.heappop(minHeap))
    # return answer
    return ans
arr = list(map(int,input().split()))
k = int(input())
s = kSorted(arr,k)
print(*s)

'''
Input:-
6 5 3 2 8 10 9
3

Output:-
2 3 5 6 8 9 10

Complexity:- O(n log k)
'''
