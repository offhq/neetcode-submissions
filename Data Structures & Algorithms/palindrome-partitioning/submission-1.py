class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            for end in range(i, len(s)):
                if s[i:end + 1] == s[i:end+1][::-1]:
                    cur.append(s[i: end + 1])
                    dfs(end + 1)
                    cur.pop()
        dfs(0)
        return res
