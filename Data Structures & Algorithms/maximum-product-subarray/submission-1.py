class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_p = float('-inf')
        max_p = 1
        min_p = 1
        for n in nums:  
            t_max = n * max_p
            max_p = max(n, t_max, n * min_p)
            min_p = min(n, t_max, n * min_p)
            best_p = max(best_p, max_p)
            
        return best_p