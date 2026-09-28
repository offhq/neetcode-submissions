class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        right_diagonals = set()
        left_diagonals = set()
        res = []
        def dfs(r):
            if r == n:
                res.append(["".join(x) for x in board])
                return
            for c in range(n):
                right_diag = r + c
                left_diag = r - c
                if c not in cols and right_diag not in right_diagonals and left_diag not in left_diagonals:
                    cols.add(c)
                    right_diagonals.add(right_diag)
                    left_diagonals.add(left_diag)
                    board[r][c] = "Q"

                    dfs(r + 1)

                    cols.remove(c)
                    right_diagonals.remove(right_diag)
                    left_diagonals.remove(left_diag)
                    board[r][c] = "."
        dfs(0)
        return res



