from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        if len(s1) > n:
            return False
        checking = False
        right = 0
        left = 0
        hashed = Counter(s1)
        while right < n:
            if not checking:
                if s2[right] in hashed:
                    hashed[s2[right]] -= 1
                    if hashed[s2[right]] == 0:
                        hashed.pop(s2[right])
                    checking = True
                    if not hashed:
                        return True
                else:
                    left += 1
            elif checking:
                if s2[right] in hashed:
                    hashed[s2[right]] -= 1
                    if hashed[s2[right]] == 0:
                        hashed.pop(s2[right])
                    if not hashed:
                        return True
                else:
                    hashed = Counter(s1)
                    checking = False
                    left += 1
                    right = left
                    continue
            right += 1
                    
        return False
