class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == "0":
                return
            state = (row, col)
            if state in visited:
                return
            visited.add(state)
            for i, j in neighbours:
                dfs(row + i, col + j)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    state = (r, c)
                    if state in visited:
                        continue
                    dfs(r, c)
                    islands += 1
        return islands

                
            
            
