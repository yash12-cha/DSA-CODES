import heapq
class Solution(object):
    def frequencySort(self, nums):
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
            heapq.heappush(maxHeap, (freq[i], (-1 *i)))
        output = []
        while maxHeap:
            # delete the elements from maxHeap one by one  based on the frequency of values               
            # and add them to resultant array
            freq, val = heapq.heappop(maxHeap)
            val *= -1
            
            for i in range(freq):
                output.append(val)
        return output	
            
