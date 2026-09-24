class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        queue = deque([])
        fresh_fruit = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if fresh_fruit == 0:
            return 0
                    
        min_elapsed = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                popped = queue.popleft()
                row = popped[0]
                col = popped[1]
                for i, j in neighbours:
                    n_row = row + i
                    n_col = col + j
                    state = (n_row, n_col)
                    
                    if n_row < 0 or n_col < 0 or n_row == rows or n_col == cols:
                        continue
                    if grid[n_row][n_col] == 1 and state not in visited:
                        visited.add(state)
                        queue.append((n_row, n_col))
                        fresh_fruit -= 1
            min_elapsed += 1
        
        if fresh_fruit != 0:
            min_elapsed = -1
        
        return min_elapsed
        