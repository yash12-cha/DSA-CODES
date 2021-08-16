n = int(input("Enter the value of N: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
x = int(input("Enter the value of X: "))
ans = 0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if Arr[i] + Arr[j] + Arr[k] == x:
                ans = 1
print(ans)
