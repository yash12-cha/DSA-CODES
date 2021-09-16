# Implementation of Linear Search
N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter elements: ").strip().split()))[:N]
K = int(input("Enter item which is to be find: "))
flag = 0
for i in range(len(Arr)):
    if Arr[i] == K:
        flag = i + 1
        break
if flag !=0:
    print("Item found at index: ",i)
else:
    print("Item not found!!!")
