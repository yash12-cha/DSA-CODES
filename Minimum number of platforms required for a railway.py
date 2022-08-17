def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    platforms = 0
    max_platforms = 0
    i, j = 0, 0
    while (i < n):
        if (arr[i] <= dep[j]):
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        elif (arr[i] > dep[j]):
            platforms -= 1
            j += 1
    return max_platforms


n = int(input("Input number of trains: "))
arr = list(map(int,input("Input arrival time of trains: ").split()))
dep = list(map(int,input("Input departure time of trains: ").split()))
res = minimumPlatform(n,arr,dep)
print("Minimum number of platforms: ",res)

'''
Input:-
Input number of trains: 6
Input arrival time of trains:  0900 0940 0950 1100 1500 1800
Input departure time of trains: 0910 1200 1120 1130 1900 2000

Output:-
Minimum number of platforms:  3
'''
