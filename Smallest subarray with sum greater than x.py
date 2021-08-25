N = int(input("Enter number of elements of array: "))
Arr1 = list(map(int,input("Enter the elements ofarray: ").strip().split()))[:N]
X = int(input("Enter value of X: "))
mini = float('inf')
for i in range(0,N):
    s = 0
    for j in range(i,N):
        s = s + Arr1[j]
        if s > X:
            mini = min(mini,j-i+1)
print("Smallest subarray with sum greater than x: ",mini)       
    
    
