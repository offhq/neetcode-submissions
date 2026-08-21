class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        htab = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if not digits:
            return[]
        def dfs(i, curr_letters):
            if i == len(digits):
                res.append(curr_letters)
                return
            for idx in range(len(htab[digits[i]])):
                dfs(i + 1, curr_letters + htab[digits[i]][idx])
        dfs(0, "")
        return res