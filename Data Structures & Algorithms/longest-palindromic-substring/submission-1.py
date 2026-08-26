class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        resLen = 0
        res = 0
        for i in range(len(s) - 1):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > resLen:
                resLen = right - left - 1
                res = left + 1

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > resLen:
                resLen = right - left - 1
                res = left + 1
        return s[res: res + resLen]


