def equilibriumPoint(A, N):
    # Find sum of the whole array
    Total = 0
    for i in range(0, N):
        Total += A[i]
    # Find cumulative sum of array
    new_list = []
    j = 0
    for i in range(0, N):
        j += A[i]
        new_list.append(j)
    # Find Left Sum
    # Find Right Sum
    # If these two sums are the same, return the element
    for i in range(0,N):
        lsum = new_list[i] - A[i]
        rsum = Total - new_list[i]
        if lsum == rsum:
            return A[i]

N = int(input("Enter number of elements: "))
A = list(map(int,input("Enter array elements: ").split()))
res = equilibriumPoint(A,N)
print("Equilibrium Point: ",res)

'''
Input:
Enter number of elements: 4
Enter array elements: 1 4 2 5

Output:
Equilibrium Point:  2

Time Complexity: O(n)
'''
