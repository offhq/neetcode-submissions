class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        search = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True

            if start in memo:
                return memo[start]
            
            for end in range(start, n):
                if s[start: end + 1] in search and dfs(end + 1):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        
        return dfs(0)

