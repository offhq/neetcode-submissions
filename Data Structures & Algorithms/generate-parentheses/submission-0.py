class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(closes: int, opens: int):
            if closes > opens or opens > n:
                return
            if len(cur) == n * 2:
                print (cur.copy())
                if closes == opens:
                    res.append("".join(cur.copy()))
                return
            cur.append("(")
            dfs(closes, opens + 1)

            cur.pop()
            cur.append(")")
            dfs(closes + 1, opens)
            cur.pop()
        dfs(0, 0)
        return res
