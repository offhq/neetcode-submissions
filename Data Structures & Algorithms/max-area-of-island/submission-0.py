class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0
            state = (row, col)
            if state in visited:
                return 0
            visited.add(state)
            area = 1
            for i, j in neighbours:
                area += dfs(row + i, col + j)
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                state = (r, c)
                if grid[r][c] == 1 and state not in visited:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area