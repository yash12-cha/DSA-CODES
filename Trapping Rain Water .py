n = int(input("Enter the value of N: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
left = [0]*n
right = [0]*n
water = 0
left[0] = Arr[0]
for i in range(1,n):
    left[i] = max(left[i-1],Arr[i])
right[n-1] = Arr[n-1]
for i in range(n-2,-1,-1):
    right[i] = max(right[i+1],Arr[i])
for i in range(0,n):
    water = water + (min(left[i],right[i]) - Arr[i])
print(water)
