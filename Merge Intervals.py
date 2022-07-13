from collections import deque
def mergeIntervals(intervals):
    # Initialise stack
    stack = deque()
    # Sort the intervals based on increasing order of starting time
    intervals.sort(key = lambda x:x[0])
    # Push the first interval on to a stack.
    stack.append(intervals[0])
    # For each interval do the following
    for i in range(1,len(intervals)):
        # Pop the top interval from stack
        ps,pe = stack.pop()
        # Extract the current interval
        cs,ce = intervals[i]
        # compare the end time of popped interval with start time of current interval
        # if the end time of popped interval is greater than or equal to the start time of current interval,then
        if pe >= cs:
            # Append to stack the start time of the popped interval as well as the maximum value
            # out of the popped interval's end time and the current interval's end time.
            stack.append([ps, max(pe, ce)])
        else:
            # Append to stack the start and end time of the popped interval
            stack.append([ps, pe])
            # Append to stack the start and end time of the current interval
            stack.append([cs, ce])
    # At the end stack contains the merged intervals
    # return stack
    return stack
n = int(input("Input number of intervals: "))
intervals = []
for i in range(n):
    ls = list(map(int,input().split()))
    intervals.append(ls)
ans = mergeIntervals(intervals)
print("Merge Intervals: ",*ans)


'''
Time Complexity:  O(nLogn)
Space Complexity: O(n)

Input number of intervals: 4
1 3
2 6
8 10
15 18
Merge Intervals:  [1, 6] [8, 10] [15, 18]
'''
