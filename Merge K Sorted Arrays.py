import heapq
def mergeKSortedArrays(nums,k):
    n = len(nums)
    # List to store answer
    result = []
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for i in range(len(nums)):
        # insert the first element of all the arrays
        # along with its indices and array number
        heapq.heappush(minHeap, (nums[i][0], i, 0))
    while len(minHeap) > 0:
        # Remove the minimum element from the heap.
        curr = heapq.heappop(minHeap)
        # i is the array number
        # j is the index of the removed element in the ith array.
        i = curr[1]
        j = curr[2]
        # Add the removed element to the output array.
        result.append(curr[0])

        # If the next element of the extracted element exists, add it to the heap.
        if j + 1 < len(nums[i]):
            heapq.heappush(minHeap, (nums[i][j + 1], i, j + 1))

    # Return the output array.
    return result
k = int(input())
lis1 = []
for i in range(k):
    lis = list(map(int, input().split()))
    lis1.append(lis)
s = mergeKSortedArrays(lis1,k)
print(*s)

'''
Input:-
3
1 4 7
3 5
2 6 7

Output:-
1 2 3 4 5 6 7 7

Time Complexity:- O((N * K) * log(K))
'''
