n = int(input("Enter the value of N: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
m = int(input("Enter the value of M: "))
# Sort the array
for i in range(len(Arr)):
    min = i
    for j in range(i+1,len(Arr)):
        if Arr[min] > Arr[j]:
            min = j
    # Swapping
    temp= Arr[i]
    Arr[i] = Arr[min]
    Arr[min] = temp
ans = float('inf') # float('inf') is used for setting a variable with an infinitely large value
for i in range(n-m+1):
        mini = Arr[i]
        maxi = Arr[i + m - 1]
        gap = maxi - mini
        if gap < ans:
            ans = gap
print("The minimum difference between maximum chocolates and minimum chocolates: ",ans)
