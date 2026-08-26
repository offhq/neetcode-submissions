class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}
        def dfs(sum_left):
            if sum_left == 0:
                return 0
            if sum_left < 0:
                return float("inf")
            if sum_left in memo:
                return memo[sum_left]
            best = float("inf")
            for coin in coins:
                best = min(best, 1 + dfs(sum_left - coin))
            memo[sum_left] = best
            return memo[sum_left]


        res = dfs(amount)
        return -1 if res == float("inf") else res
