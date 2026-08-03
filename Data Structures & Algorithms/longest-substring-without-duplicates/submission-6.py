class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if n <= 1:
            return n

        left = 0
        res = 0
        uniques = set()

        for right in range(n):
    
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1

            uniques.add(s[right])

            res = max(res, right - left + 1)
      


        return res
        

