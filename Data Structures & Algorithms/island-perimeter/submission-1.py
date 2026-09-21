class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:    
        rows = len(grid)
        cols = len(grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = {}
        perimeter = 0

        def dfs(row, col):
            nonlocal perimeter
            if row == rows or col == cols or row < 0 or col < 0:
                return 1
            state = (row, col)

            if state in visited:
                return visited[state]
            visited[state] = 0 if grid[row][col] == 1 else 1

            square_perim = 0
            if grid[row][col] == 1:
                for i, j in neighbours:
                    square_perim += dfs(row + i, col + j)
                perimeter += square_perim

                return 0

            return 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return perimeter
        return 0

        



            
            