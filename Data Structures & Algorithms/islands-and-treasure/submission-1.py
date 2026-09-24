from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

                    
        
        curr_d = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                popped = queue.popleft()
                row = popped[0]
                col = popped[1]
                state = (row, col)
                if state in visited:
                    continue
                visited.add(state)
                grid[row][col] = min(grid[row][col], curr_d)
                for i, j in neighbours:
                    n_row = row + i
                    n_col = col + j
                    
                    
                    if n_row < 0 or n_col < 0 or n_row == rows or n_col == cols or grid[n_row][n_col] == -1:
                        continue

                    
                    queue.append((n_row, n_col))
            curr_d += 1


            


            