from typing import List

from typing import List

class MinCostTickets:
    def mincost_tickets(self, travel_days: List[int], pass_costs: List[int]) -> int:
        total_days = len(travel_days)
        dp = [0] * (total_days + 1)  # Initialize dp with size total_days + 1

        for k in range(total_days - 1, -1, -1):
            # Option 1: Buy a 1-day pass
            cost_with_1_day_pass = pass_costs[0] + dp[k + 1]

            # Option 2: Buy a 7-day pass
            next_index = k
            while next_index < total_days and travel_days[next_index] < travel_days[k] + 7:
                next_index += 1
            cost_with_7_day_pass = pass_costs[1] + dp[next_index]

            # Option 3: Buy a 30-day pass
            next_index = k
            while next_index < total_days and travel_days[next_index] < travel_days[k] + 30:
                next_index += 1
            cost_with_30_day_pass = pass_costs[2] + dp[next_index]

            dp[k] = min(cost_with_1_day_pass, cost_with_7_day_pass, cost_with_30_day_pass)

        return dp[0]


# Example usage:
travel_days = [1, 4, 6, 7, 8, 20]
pass_costs = [2, 7, 15]
min_cost_tickets = MinCostTickets()
minimum_cost = min_cost_tickets.mincost_tickets(travel_days, pass_costs)

'''
Time Complexity: O(N)
-> The algorithm iterates through each travel day once, performing constant-time operations for each.

Space Complexity: O(N)
-> A dp array of size N is used to store the minimum cost up to each travel day.
'''
