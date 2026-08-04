class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        left = 0
        res = 0
        counts  = {}


        for right in range(n):
            if s[right] not in counts:
                counts[s[right]] = 0
            counts[s[right]] += 1
            while sum(counts.values()) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res