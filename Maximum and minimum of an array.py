N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
min = Arr[0]
max = Arr[0]
# Minimum Element
for i in range(N):
    if Arr[i] < min:
        min = Arr[i]
# Maximum Element
for i in range(N):
    if Arr[i] > max:
        max = Arr[i]
print("Minimum Element:",min)
print("Maximum Element:",max)
