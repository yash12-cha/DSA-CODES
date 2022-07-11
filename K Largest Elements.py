import heapq
def KLargest(N,X,k):
    minHeap = []
    heapq.heapify(minHeap)
    ans = []
    for i in range(N):
        heapq.heappush(minHeap,X[i])
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    for i in minHeap:
        ans.append(i)
    return ans

N = int(input("Enter size of list: "))
k = int(input("Enter value of k: "))
print("Enter list elements: ",end = " ")
X = list(map(int,input().split()))
ans = KLargest(N,X,k)
print("K Largest elements: ",end = " ",*ans)

'''
Enter size of list: 6
Enter value of k: 3
Enter list elements:  7 10 4 3 20 15
K Largest elements:  10 15 20 
'''

'''
Time Complexity: O(nlogk)
'''
