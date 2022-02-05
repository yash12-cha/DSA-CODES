class Solution(object):
    def merge(self, intervals):
        # Sort the intervals based on increasing order of starting time
        intervals.sort(key = lambda x : x[0])
        # Push the first interval on to the stack.
        st = [intervals[0]]
        # For each interval do the following
        for i in range(1, len(intervals)):
            # Pop the top interval from stack
            ps,pe = st.pop()
            # Extract the current interval
            cs,ce = intervals[i]
            # compare the end time of popped interval with start time of current interval
            # if the end time of popped interval is greater than or equal to the start time of current interval,then
            if pe >= cs:
                # Append to stack the start time of the popped interval as well as the maximum value out of the popped interval's end time and the current interval's                         end time. 
                st.append([ps, max(pe, ce)])
            else:
                # Append to stack the start and end time of the popped interval
                st.append([ps, pe])
                # Append to stack the start and end time of the current interval
                st.append([cs, ce])
        # At the end stack contains the merged intervals
        # return stack
        return st
