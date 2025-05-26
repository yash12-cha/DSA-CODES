from typing import List

class MinCostTickets:
    def solve(self, travel_days: List[int], pass_costs: List[int], current_index: int) -> int:
        total_days = len(travel_days)
        if current_index >= total_days:
            return 0

        # Option 1: Buy a 1-day pass
        cost_with_1_day_pass = pass_costs[0] + self.solve(travel_days, pass_costs, current_index + 1)

        # Option 2: Buy a 7-day pass
        next_index = current_index
        while next_index < total_days and travel_days[next_index] < travel_days[current_index] + 7:
            next_index += 1
        cost_with_7_day_pass = pass_costs[1] + self.solve(travel_days, pass_costs, next_index)

        # Option 3: Buy a 30-day pass
        next_index = current_index
        while next_index < total_days and travel_days[next_index] < travel_days[current_index] + 30:
            next_index += 1
        cost_with_30_day_pass = pass_costs[2] + self.solve(travel_days, pass_costs, next_index)

        return min(cost_with_1_day_pass, cost_with_7_day_pass, cost_with_30_day_pass)

    def mincostTickets(self, travel_days: List[int], pass_costs: List[int]) -> int:
        return self.solve(travel_days, pass_costs, 0)

# Example usage:
travel_days = [1, 4, 6, 7, 8, 20]
pass_costs = [2, 7, 15]
min_cost_tickets = MinCostTickets()
minimum_cost = min_cost_tickets.mincostTickets(travel_days, pass_costs)

'''
Time Complexity: O(3^N)

-> At each travel day, there are up to three choices: buy a 1-day, 7-day, or 30-day pass. This leads to a branching factor of 3.
-> With N travel days, the total number of recursive calls can be up to 3^N.

Space Complexity: O(N)

-> The maximum depth of the recursion stack is N, corresponding to the number of travel days.
'''
