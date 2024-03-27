class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            # Update the cost of reaching the current step
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum cost of reaching either the first or second step
        x = int(f"{min(cost[0], cost[1])}")
        return x
