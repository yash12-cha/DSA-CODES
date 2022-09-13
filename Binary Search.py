def binarysearch(arr, n, k):
	    start = 0
	    end = n - 1
	    while(start <= end):
	        mid  = start + (end - start)//2
	        if (k == arr[mid]):
	            return mid
	        elif(k > arr[mid]):
	            start = mid + 1
	        else:
	            end = mid - 1
	    return -1
N = int(input("Input size of array: "))
arr = list(map(int,input("Input Array: ").split()))
k = int(input("Input element to search: "))
res = binarysearch(arr,N,k)
print("Position at which",k,"is present: ",res)

'''
Input:-
Input size of array: 5
Input Array: 1 2 3 4 5
Input element to search: 4

Output:-
Position at which 4 is present:  3

Time Complexity: O(log n)
'''

'''
Note: Here we are using 
	mid = start + (end – start)//2

Maybe, you wonder why we are calculating the middle index this way, we can simply add the start and end index and divide it by 2.
    	mid = (start + end)//2
	
But if we calculate the middle index like this means our code is not 100% correct, it contains bugs. 
That is, it fails for larger values of int variables start and end. 
Specifically, it fails if the sum of start and end is greater than the maximum positive int value(2^31 – 1 ).
The sum overflows to a negative value and the value stays negative when divided by 2.

    					mid = start + (end – start)//2
					
So it’s better to use it like this. This bug applies equally to merge sort and other divide and conquer algorithms.
'''



