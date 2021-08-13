N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
k = int(input("Enter the vale of k: "))
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
# Kth smallest element 
for i in range(N):
    if i == k-1:
        print("Kth smallest element: ",Arr[i])
#Kth largest element
while(N):
    if N == k:
        print("Kth largest element: ",Arr[N])
        break
    N = N - 1
