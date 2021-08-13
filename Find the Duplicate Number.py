N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
for i in range(N):
    min = i
    for j in range(i+1,N):
        if Arr[min] > Arr[j]:
            min = j
    # Swapping
    temp= Arr[i]
    Arr[i] = Arr[min]
    Arr[min] = temp
for i in range(0,N-1):
    if Arr[i] == Arr[i+1]:
        flag = Arr[i]
        break
print(flag)  
