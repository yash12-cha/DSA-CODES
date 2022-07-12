import heapq
def maxItems(ls,k):
    minHeap = []
    sum = 0
    count = 0
    heapq.heapify(minHeap)
    for i in range(len(ls)):
        heapq.heappush(minHeap,ls[i])
    for i in range(len(minHeap)):
        p = heapq.heappop(minHeap)
        sum += p
        if sum <= k:
            count += 1
        else:
            break
    return count
k = int(input("Enter the value of sum: "))
ls = list(map(int,input("Input Items: ").split()))
ans = maxItems(ls,k)
print("Maximum items with given sum: ",ans,end= " ")

'''
Enter the value of sum: 50
Input Items: 1 12 5 111 200 1000 10
Maximum items with given sum:  4 

Time Complexity: O(N*logN)
'''
