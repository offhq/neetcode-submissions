class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, maxLen = 0, 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] =True
                if maxLen < 2:
                    maxLen = 2
                    res = i
        
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if maxLen < k:
                        maxLen = k
                        res = i
        return s[res: res + maxLen]

