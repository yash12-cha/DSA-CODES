def pageFaults(C, pages):
    faults = 0
    s = []
    for i in pages:
        # If element is not present in memory
        if i not in s:
            # If memory is full
            if len(s) == C:
                # Remove the first element
                # As it is least recently used
                s.pop(0)
                # Add the recent element into memory
                s.append(i)
            # If memory is not full
            else:
                # Add the recent element into memory
                s.append(i)
            # Count the number of faults
            faults += 1
        # If element is present in memory
        else:
            # If element is present
            # Remove the element
            s.remove(i)
            # And add it at the end as it is the most recent element
            s.append(i)

    return faults
N = int(input("Input length: "))
C = int(input("Input memory capacity: "))
pages = list(map(int,input("Input sequence of pages: ").split()))
res = pageFaults(C, pages)
print("Page Faults: ",res,end=" ")

'''
Input: -
Input length: 9
Input memory capacity: 4
Input sequence of pages: 5 0 1 3 2 4 1 0 5

Output:-
Page Faults:  8 

Time Complexity: O(N)
'''
