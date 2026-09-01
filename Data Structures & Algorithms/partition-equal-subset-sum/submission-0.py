class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total /2
        n = len(nums)
        memo = {}
        def dfs(i, cur_sum):
            if i >= n:
                return False
            if cur_sum == half:
                return True
            state = (i, cur_sum)
            if state in memo:
                return memo[state]
            memo[state] = dfs(i + 1, cur_sum + nums[i]) or dfs(i + 1, cur_sum)
            return memo[state]
        return dfs(0, 0)
