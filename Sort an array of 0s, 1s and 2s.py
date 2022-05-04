 # Method 1: Keeping count of values
    
def sortColors(self, arr):
        n = len(arr)
        c0 = 0
        c1 = 0
        c2 = 0
        for i in range(n):
            if arr[i] == 0:
                c0 += 1
            if arr[i] == 1:
                c1 += 1
            if arr[i] == 2:
                c2 += 1
        k = 0
        for i in range(c0):
            arr[k] = 0
            k += 1
        for i in range(c1):
            arr[k] = 1
            k += 1
        for i in range(c2):
            arr[k] = 2
            k += 1


# Method 2: 3-Pointer approach

def sortColors(self, arr):
        n = len(arr)
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            elif arr[mid] == 2:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
