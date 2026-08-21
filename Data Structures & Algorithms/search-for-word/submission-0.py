class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols = len(board[0])
        rows = len(board)
        visited = set()
        def dfs(i, row, col):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[i] or (row, col) in visited:
                return False
            
            visited.add((row, col))

            directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]

            for dr, dc in directions:
                if dfs(i + 1, row + dr, col + dc):
                    return True
            
            visited.remove((row, col))

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True

        return False


            



