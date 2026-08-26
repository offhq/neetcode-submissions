class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recur(step):
            if step <= 2:
                return step
            if step in memo:
                return memo[step]
            memo[step] = recur(step - 1) + recur(step - 2)
            return memo[step]
        return recur(n)
