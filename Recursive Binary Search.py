def recursivebinarysearch(arr,start,end,key):
    # Base Case
    # Only one element present
    if (start == end):
        if (arr[start] == key):
            return start
        else:
            return -1
    else:
        mid = (start + end)//2
        if (key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return recursivebinarysearch(arr, start, mid - 1, key)
        else:
            return recursivebinarysearch(arr, mid + 1, end, key)
    return -1

arr = list(map(int,input("Input Array: ").split()))
key = int(input("Input element to search: "))
start = 0
end = len(arr) - 1
res = recursivebinarysearch(arr,start,end,key)
if res != -1:
    print("Position at which", key, "is present: ", res+1)
else:
    print("Element not found!!!")

