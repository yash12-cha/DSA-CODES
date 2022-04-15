import heapq
def findKClosestElements(arr, k, x):
    # Declare empty list
    maxHeap = []
    # using heapify to convert list into heap
    heapq.heapify(maxHeap)
    for i in range(len(arr)):
        # Insert into Heap
        # the absolute value of the difference of x with current element
        # and the current element
        heapq.heappush(maxHeap, (-1 * abs(x - arr[i]), -1 * arr[i]))
        if len(maxHeap) > k:
            # removes the largest element from the max heap
            heapq.heappop(maxHeap)
    res = []
    for diff, val in maxHeap:
        res.append(-1 * val)
    res.sort()
    return res
lis = list(map(int, input().split()))
k = int(input())
x = int(input())
s = findKClosestElements(lis,k,x)
print(*s)


'''
Input:-
5 6 7 8 9
3
7

Output:-
6 7 8

Time Complexity:- O(n Log k)
'''
