N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
K = int(input("Enter the value of K: "))
c = 0
for i in range(N):
    for j in range(i+1,N):
        if Arr[i] + Arr[j] == K:
            c = c + 1
print("Number of pair of elements in the array whose sum is equal to K: ",c)
