def nextSmallerElementToTheLeft(arr):
    nselIndex = []
    s = []
    n = len(arr)
    for i in range(0, n,1):
        while (len(s) != 0 and s[-1][0] >= arr[i]):
            s.pop()
        if len(s) == 0:
            nselIndex.append(-1)
        else:
            nselIndex.append(s[-1][1])
        s.append([arr[i], i])
    return nselIndex


def nextSmallerElementToTheRight(arr):
    nserIndex = []
    s = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and s[-1][0] >= arr[i]):
            s.pop()
        if len(s) == 0:
            nserIndex.append(len(arr))
        else:
            nserIndex.append(s[-1][1])
        s.append([arr[i], i])
    nserIndex.reverse()
    return nserIndex


def maxAreaHistogram(heights):
    left = nextSmallerElementToTheLeft(heights)
    right = nextSmallerElementToTheRight(heights)
    width = []
    maxArea = 0
    Area = []
    for i in range(len(heights)):
        width.append((right[i] - left[i] - 1))
        Area.append(width[i] * heights[i])
        if (maxArea < Area[i]):
            maxArea = Area[i]
    return maxArea
n = int(input())
heights = list(map(int,input().split()))
a = maxAreaHistogram(heights)
print(a)


'''
Input: -
6
2 1 5 6 2 3

Output: -
10

Time Complexity: O(N), where N is the size of the array
'''
