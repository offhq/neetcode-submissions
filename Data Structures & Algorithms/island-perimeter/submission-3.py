class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:    
        rows = len(grid)
        cols = len(grid[0])
        neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()


        def dfs(row, col):
            if row == rows or col == cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 1
            
            state = (row, col)
            if state in visited:
                return 0
            visited.add(state)

            perim = 0

            for i, j in neighbours:
                perim += dfs(row + i, col + j)

            return perim


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
        return 0

        



            
            