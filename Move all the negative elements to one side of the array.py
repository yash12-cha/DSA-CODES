N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
i = -1
pivot = 0 # Pivot element
for j in range(0, N) :
        if (Arr[j] < pivot) :
            i = i + 1
            temp = Arr[i]
            Arr[i] = Arr[j]
            Arr[j]= temp
print(*Arr)   
    
