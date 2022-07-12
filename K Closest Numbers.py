import heapq
def findClosestElements(arr, k, x):
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for i in range(len(arr)):
        # Insert into Heap
        # the absolute value of the difference of x with current element
        # and the current element
        heapq.heappush(minHeap, (abs(x - arr[i]), arr[i]))
    res = []
    for j in range(k):
        diff, val = heapq.heappop(minHeap)
        res.append(val)
    res.sort()
    return res
k = int(input("Enter value of k: "))
x = int(input("Enter value of x: "))
ls = list(map(int,input("Input List: ").split()))
c = findClosestElements(ls,k,x)
print("K closest numbers: ",*c,end=" ")


'''
Enter value of k: 3
Enter value of x: 7
Input List: 5 6 7 8 9
K closest numbers:  6 7 8 

Time Complexity:- O(n Log k)
'''
