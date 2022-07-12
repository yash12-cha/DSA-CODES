import heapq
def frequencySort(nums):
    # Declare empty list
    maxHeap = []
    # using heapify to convert list into heap
    heapq.heapify(maxHeap)
    # insert all elements and their counts into a hash
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # store the contents of hash in a maxHeap
    for i in freq:
        heapq.heappush(maxHeap, (-1 * freq[i], (i)))
    output = []
    while maxHeap:
        # delete the elements from maxHeap one by one  based on the frequency of values
        # and add them to resultant array
        freq, val = heapq.heappop(maxHeap)
        freq *= -1

        for i in range(freq):
            output.append(val)
    return output

lis = list(map(int, input().split()))
s = frequencySort(lis)
print(*s)

'''
Input:-
2 3 1 3 2

Output:-
1 3 3 2 2

Time Complexity:- O(N log N + N)
'''

