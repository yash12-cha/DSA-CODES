def majorityElement(A,N):
    hashmap = {}
    for i in A:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for j in hashmap:
        if hashmap[j] > N / 2:
            return j
    return -1

Arr = list(map(int,input("Input Array: ").split()))
N = int(input("Input N: "))
res = majorityElement(Arr,N)
if res == -1:
    print("No Majority Element.")
else:
    print("Majority Element: ",res)


'''
Time Complexity: O(n), One traversal of the array is needed, so the time complexity is linear.
Auxiliary Space: O(n), Since a hashmap requires linear space.
'''
