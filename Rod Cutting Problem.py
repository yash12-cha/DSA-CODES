def cutRod(price, n):
    length = []
    for i in range(1, n + 1):
        length.append(i)
    l = len(length)
    dp = [[0 for i in range(l + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, l + 1):
            if length[i - 1] <= j:
                dp[i][j] = max(price[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][l]
N = int(input("Enter length of rod: "))
E = list(map(int,input("Enter price of all pieces: ").split()))
res = cutRod(E,N)
print("Maximum value obtained by cutting up the rod and selling the pieces: ",res)

'''
Input:
Enter length of rod: 8
Enter price of all pieces: 1 5 8 9 10 17 17 20

Output:
Maximum value obtained by cutting up the rod and selling the pieces:  22

Time Complexity: O(n^2)
'''
