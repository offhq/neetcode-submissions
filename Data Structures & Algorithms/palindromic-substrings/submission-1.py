class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1
        
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
        return res