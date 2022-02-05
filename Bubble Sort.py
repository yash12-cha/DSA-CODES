N = int(input())
Arr = list(map(int,input().split()))
count = 0
for i in range(N-1):
    swapped = False
    # Since, after each iteration right most i elements are sorted 
    for j in range(0,N - i - 1):
        if Arr[j] > Arr[j+1]:
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp
            swapped = True
            count += 1
    # If no number was swapped that means array is sorted now, break the loop.
    if swapped == False:
        break
print("Array is sorted in",count,"swaps.")
print("First Element:",Arr[0])
print("Last Element:",Arr[N-1])
