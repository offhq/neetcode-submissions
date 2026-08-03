class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 1
        res = 0
        

        if n <= 1:
            return n

        uniques = set()
        uniques.add(s[left])
        while right < n:
            
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1
            uniques.add(s[right])
            length = right - left + 1
            if length > res:
                res = length
            right += 1

        return res
        

