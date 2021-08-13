N = int(input("Enter number of elements of first array: "))
Arr1 = list(map(int,input("Enter the elements of first array: ").strip().split()))[:N]
M = int(input("Enter number of elements of second array: "))
Arr2 = list(map(int,input("Enter the elements of second array: ").strip().split()))[:M]
union_array = [ ]
intersection_array = [ ]
# Union of two array
p = 0 
q = 0
while ((p < N) and (q < M)):
    if Arr1[p] < Arr2[q]:
        union_array.append(Arr1[p])
        p = p + 1
    elif Arr1[p] > Arr2[q]:
        union_array.append(Arr2[q])
        q = q + 1
    else:
        union_array.append(Arr1[p])
        p = p + 1
        q = q + 1
# Remaining elements
while p < N:
    union_array.append(Arr1[p])
    p = p + 1
while q < M:
    union_array.append(Arr2[q])
    q = q + 1
print("Union of the given two array: ")
print(*union_array)
# Intersection of two array
for i in range(N):
    for j in range(M):
        if Arr1[i] == Arr2[j]:
            intersection_array.append(Arr1[i])
print("Intersection of the given two array: ")
print(*intersection_array)
            
    
