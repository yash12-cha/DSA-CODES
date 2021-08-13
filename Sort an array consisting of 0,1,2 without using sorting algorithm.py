N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
c0 = 0
c1 = 0
c2 = 0
for i in range(N):
    if Arr[i] == 0:
        c0 = c0 + 1
    if Arr[i] == 1:
        c1 = c1 + 1
    if Arr[i] == 2:
        c2 = c2 + 1
k = 0
for i in range(c0):
    Arr[k] = 0
    k = k + 1
for i in range(c1):
    Arr[k] = 1
    k = k + 1
for i in range(c2):
    Arr[k] = 2
    k = k + 1
for i in range(N):
    print(Arr[i])

    
