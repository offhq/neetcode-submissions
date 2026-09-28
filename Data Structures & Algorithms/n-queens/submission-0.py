class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        rows = set()
        cols = set()
        right_diagonals = set()
        left_diagonals = set()
        res = []
        def dfs(r):
            if r == n:
                res.append(["".join(x) for x in board])
                return
            for col in range(n):
                right_diag = r + col
                left_diag = r - col
                if r not in rows and col not in cols and right_diag not in right_diagonals and left_diag not in left_diagonals:
                    rows.add(r)
                    cols.add(col)
                    right_diagonals.add(right_diag)
                    left_diagonals.add(left_diag)
                    board[r][col] = "Q"

                    dfs(r + 1)

                    rows.remove(r)
                    cols.remove(col)
                    right_diagonals.remove(right_diag)
                    left_diagonals.remove(left_diag)
                    board[r][col] = "."
        dfs(0)
        return res



