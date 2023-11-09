def minTaps(n, ranges):
    # Initialize variables to keep track of covered range and opened taps
    mini = 0  # Leftmost point of currently covered range
    maxi = 0  # Rightmost point of currently covered range
    open_tap = 0  # Number of taps opened

    # Continue while the rightmost point is less than n (total range to be covered)
    while (maxi < n):
        # Iterate through the list of tap ranges
        for i in range(0, len(ranges)):
            # Check if the range of the current tap can extend the coverage to the right
            if ((i - ranges[i] <= mini) and (i + ranges[i] > maxi)):
                maxi = i + ranges[i]  # Update the rightmost point of the covered range

        # If the leftmost and rightmost points are the same, it means no further coverage can be achieved
        if (mini == maxi):
            return -1  # Return -1 to indicate that it's not possible to cover the entire range

        # Increment the count of opened taps and update the leftmost point of the covered range
        open_tap += 1
        mini = maxi

    # Return the count of opened taps, which is the minimum number of taps required
    return open_tap


# Input the total range (n) and the ranges of individual taps as a list
n = int(input("Input length of the garden: "))
ranges = list(map(int, input("Ranges of taps: ").split()))

# Call the minTaps function with the provided input to get the result
result = minTaps(n, ranges)
print("Minimum number of taps required:", result)

'''
Time Complexity: Since the for loop is nested within the while loop, the overall time complexity is O(n^2).
'''
