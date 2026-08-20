class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        
        # Track the remaining target instead of calculating sum(cur)
        def dfs(i, target_left):
            # Base Case: We hit the exact target
            if target_left == 0:
                res.append(cur.copy())
                return
            
            # Base Case: Exceeded target (since all numbers are positive) or out of bounds
            if target_left < 0 or i >= len(nums):
                return
            
            # Decision 1: Include nums[i] and stay at index i (allows reuse)
            cur.append(nums[i])
            dfs(i, target_left - nums[i]) 
            
            # Decision 2: Exclude nums[i] and move to the next index
            cur.pop()
            dfs(i + 1, target_left)
            
        # Start with the full target value
        dfs(0, target)
        return res