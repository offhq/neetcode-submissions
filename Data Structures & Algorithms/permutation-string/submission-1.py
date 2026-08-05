from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        c1 = Counter(s1)
        win = Counter(s2[:len1])
        if c1 == win:
            return True
        for i in range (len1, len2):
            win[s2[i]] += 1
            left_char = s2[i-len1]
            win[left_char] -= 1
            if win[left_char] == 0:
                del win[left_char]
            if c1 == win:
                return True
        return False

