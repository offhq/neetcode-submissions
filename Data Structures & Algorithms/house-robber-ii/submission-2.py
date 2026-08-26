class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, fh = False):
            if i == len(nums) - 1 and fh and i != 0:
                return 0
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dfs(i + 2, fh), dfs(i + 3, fh))
            return memo[i]
        cur_res = max(dfs(0, True), dfs(1))
        nums.reverse()
        memo = {}
        return max(cur_res, dfs(0, True))