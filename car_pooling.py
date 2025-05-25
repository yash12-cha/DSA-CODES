
from collections import defaultdict
def carPooling(trips, capacity):
    # Dictionary to record net passenger changes at each location
    passenger_changes = defaultdict(int)

    # Record the net change in passengers at each location
    for num_passengers, start, end in trips:
        passenger_changes[start] += num_passengers
        passenger_changes[end] -= num_passengers

    # Track the current number of passengers in the car
    current_passengers = 0
    # Process the locations in order
    for location in sorted(passenger_changes):
        current_passengers += passenger_changes[location]
        if current_passengers > capacity:
            return False

    return True

trips = [[2,1,5],[3,3,7]]
capacity = 5
ans = carPooling(trips,capacity)

'''
⏱ Time Complexity: O(n log n)

-> Processing Trips: For each of the n trips, we perform constant-time operations to update the dictionary, resulting in O(n) time.
-> Sorting Locations: We sort the keys of the dictionary to process locations in order. If there are k unique locations, this takes O(k log k) time. In the worst case, where each trip has unique start and end locations, k can be up to 2n, leading to O(n log n) time.
-> Total Time: Combining both steps, the total time complexity is O(n + n log n) = O(n log n).

🧠 Space Complexity: O(k)

-> Passenger Changes Dictionary: We store only the net passenger changes at each unique location, requiring O(k) space, where k is the number of unique locations. In the worst case, k can be up to 2n.
-> Auxiliary Variables: We use a few additional variables (current_passengers, etc.), which consume constant space.
-> Total Space: Therefore, the total space complexity is O(k).
'''