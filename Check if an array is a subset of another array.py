# Python program to check if an array is a subset of another
M = int(input("Enter number of elements of first array: "))
Arr1 = list(map(int,input("Enter the elements of first array: ").strip().split()))[:M]
N = int(input("Enter number of elements of second array: "))
Arr2 = list(map(int,input("Enter the elements of second array: ").strip().split()))[:N]
Arr1.sort()
Arr2.sort()
i = 0
j = 0
count = 0
while i < M and j < N:
    if Arr1[i] == Arr2[j]:
        count = count + 1
        i = i + 1
        j = j + 1 
    else:
        i = i + 1
if count == N:
    print("Array2 is a subset of Array1.")
else:
    print("Array2 is not a subset of Array1.")
