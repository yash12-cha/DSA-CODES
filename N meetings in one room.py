def maxMeetings(n,start,end):
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
    output.append(i+1)
    for j in range(1, len(a)):
        if a[j][0] >= a[i][1]:
            output.append(j+1)
            i = j
    return output
n = int(input("Input number of meetings: "))
start = list(map(int,input("Input start time of meetings: ").split()))
end = list(map(int,input("Input end time of meetings: ").split()))
res = maxMeetings(n,start,end)
print("Following meetings are selected: ",*res,end=" ")


'''
Input:-
Input number of meetings: 6
Input start time of meetings: 1 3 0 5 8 5
Input end time of meetings: 2 4 6 7 9 9
Output:-
Following meetings are selected:  1 2 4 5
'''



'''
Time Complexity:
    Case 1 : O(N), in case, the given array is sorted according to their finish times, where N is total steps.
    Case 2 : O(NlogN), in case, the given array is not sorted according to their finish times, where N is total steps.
    
'''
