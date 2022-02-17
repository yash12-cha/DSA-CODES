def activitySelection(n, start, end):
    # Combine start and end time of activities in single list
    a = []
    for i in range(0, n):
        l = []
        l.append(start[i])
        l.append(end[i])
        a.append(l)
    # Sort the activities according to their end time
    a.sort(key=lambda x: x[1])
    i = 0
    output = []
    output.append(i)
    for j in range(1, len(a)):
        if a[j][0] >= a[i][1]:
            output.append(j)
            i = j
    return output
n = int(input())
s = list(map(int,input().split()))
e = list(map(int,input().split()))
res = activitySelection(n,s,e)
print(res)
