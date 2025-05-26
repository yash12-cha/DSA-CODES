from typing import List

class MinCostTickets:
    def solve_mem(self, travel_days: List[int], pass_costs: List[int], current_index: int, dp: List[int]) -> int:
        total_days = len(travel_days)
        if current_index >= total_days:
            return 0
        if dp[current_index] != -1:
            return dp[current_index]

        # Option 1: Buy a 1-day pass
        cost_with_1_day_pass = pass_costs[0] + self.solve_mem(travel_days, pass_costs, current_index + 1, dp)

        # Option 2: Buy a 7-day pass
        next_index = current_index
        while next_index < total_days and travel_days[next_index] < travel_days[current_index] + 7:
            next_index += 1
        cost_with_7_day_pass = pass_costs[1] + self.solve_mem(travel_days, pass_costs, next_index, dp)

        # Option 3: Buy a 30-day pass
        next_index = current_index
        while next_index < total_days and travel_days[next_index] < travel_days[current_index] + 30:
            next_index += 1
        cost_with_30_day_pass = pass_costs[2] + self.solve_mem(travel_days, pass_costs, next_index, dp)

        dp[current_index] = min(cost_with_1_day_pass, cost_with_7_day_pass, cost_with_30_day_pass)
        return dp[current_index]

    def mincost_tickets(self, travel_days: List[int], pass_costs: List[int]) -> int:
        dp = [-1] * len(travel_days)
        return self.solve_mem(travel_days, pass_costs, 0, dp)

# Example usage:
travel_days = [1, 4, 6, 7, 8, 20]
pass_costs = [2, 7, 15]
min_cost_tickets = MinCostTickets()
minimum_cost = min_cost_tickets.mincost_tickets(travel_days, pass_costs)


'''
Time Complexity: O(N)

-> Each subproblem (defined by the current index in the travel_days list) is solved only once and stored in a memoization table.
-> Thus, the total number of computations is linear with respect to the number of travel days.

Space Complexity: O(N)

-> Space is used for the memoization table (dp array) and the recursion stack, each of which can grow up to size N.
'''
