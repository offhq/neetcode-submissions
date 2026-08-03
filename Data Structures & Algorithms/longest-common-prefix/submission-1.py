class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):

            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:-1]
        return prefix

            
        