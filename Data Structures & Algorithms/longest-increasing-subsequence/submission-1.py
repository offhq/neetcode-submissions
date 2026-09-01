class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(j, i):
            if i >= n:
                return 0
            curr = (j, i)
            if curr in memo:
                return memo[curr]
            skip = dfs(j, i + 1)
            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + dfs(i, i + 1)
            memo[curr] = max(take, skip)
            return memo[curr]
            
        
        return dfs(-1, 0)