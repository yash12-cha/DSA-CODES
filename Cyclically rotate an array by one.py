N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
last = Arr[N-1]
for i in range(N-1,0,-1):
    Arr[i] = Arr[i-1]
Arr[0] = last
print(*Arr)
    
