import heapq
def SortByFrequency(arr):
    n = len(arr)
    hash = {}
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    # Declare empty list
    maxHeap = []
    # using heapify to convert list into heap
    heapq.heapify(maxHeap)
    for r in hash:
        # Adding items to the heap using heappush
        # function by multiplying them with -1
        heapq.heappush(maxHeap, [-hash[r], r])
    ans = []
    while maxHeap:
        freq, ele = heapq.heappop(maxHeap) # Get the element with highest frequency
        for i in range(-freq):
            ans.append(ele)
    return ans
arr = list(map(int,input("Input Array: ").split()))
res = SortByFrequency(arr)
print("Sorting Elements of Array by Frequency: ",*res)

'''
Time Complexity: O(n * log(n))
Space Complexity: O(n)
'''
