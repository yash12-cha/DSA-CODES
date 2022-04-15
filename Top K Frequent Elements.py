import heapq


def topKFrequent(nums, k):
    # Count the frequency of elements and store in hashmap
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for i in freq:
        # Insert into Heap element-frequency pair
        heapq.heappush(minHeap, (freq[i], i))
        if len(minHeap) > k:
            # removes the smallest element from the min heap
            heapq.heappop(minHeap)
    res = []
    for fre, val in minHeap:
        res.append(val)
    res.sort()
    return res
lis = list(map(int, input().split()))
k = int(input())
s = topKFrequent(lis,k)
print(*s)

'''
Input:-
1 1 1 3 2 2 4
2

Output:-
1 2

Time Complexity:- O(k log N + N), here N is the number of elements. Because in the worst-case all of the numbers present in the input might be distinct.
'''
