class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []

        def dfs(i, target_left):

            if target_left == 0:
                res.append(cur.copy())
                return
            
            if target_left < 0 or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, target_left - candidates[i]) 

            cur_num = cur.pop()
            n = 1
            while i + n < len(candidates) and candidates[i + n] == cur_num:
                n += 1
            dfs(i + n, target_left)

        dfs(0, target)

        return res