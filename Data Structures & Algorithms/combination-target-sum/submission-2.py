class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, target_left):

            if target_left == 0:
                res.append(cur.copy())
                return
            

            if target_left < 0 or i >= len(nums):
                return

            cur.append(nums[i])
            dfs(i, target_left - nums[i]) 

            cur.pop()
            dfs(i + 1, target_left)

        dfs(0, target)
        return res