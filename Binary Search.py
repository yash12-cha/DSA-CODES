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

