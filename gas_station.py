from typing import List

class GasStationCircuit:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas_available = sum(gas)
        total_gas_required = sum(cost)
        
        if total_gas_available < total_gas_required:
            return -1  # Not possible to complete the circuit

        starting_station = 0
        current_fuel_balance = 0

        for station_index in range(len(gas)):
            current_fuel_balance += gas[station_index] - cost[station_index]

            if current_fuel_balance < 0:
                # Can't reach the next station from here, reset start
                starting_station = station_index + 1
                current_fuel_balance = 0

        return starting_station

circuit = GasStationCircuit()
print(circuit.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3

# Time complexity: O(n)
# Space complexity: O(1)