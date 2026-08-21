class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1)
            s = cur.pop()
            n = 1
            while i + n < len(nums) and nums[i + n] == s:
                n += 1
            dfs(i + n)
        dfs(0)
        return res



        