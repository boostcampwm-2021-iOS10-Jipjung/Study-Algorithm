from collections import deque

class Solution:
    DIRECTION = ((1, 0), (0, 1))
    def gridGame(self, grid: List[List[int]]) -> int:
        b_scores = []
        next_grid = [grid[0][:], [0] * len(grid[0])]
        next_grid[0][0] = 0
        self.find_max(next_grid)
        
        b_scores.append(self.find_max(next_grid))
        for j in range(1, len(grid[0])):
            next_grid[0][j] = 0
            next_grid[1][j - 1] = grid[1][j - 1]
            b_scores.append(self.find_max(next_grid))
        # print(b_scores)    
        return min(b_scores)
    
    def find_max(self, grid):
        q = deque()
        q.append((0, 0, 0))
        answer = []
        while q:
            i, j, v = q.popleft()
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                 answer.append(v)
            for di, dj in self.DIRECTION:
                 ni, nj = i + di, j + dj
                 if 0 > ni or ni >= len(grid) or 0 > nj or nj >= len(grid[0]):
                    continue
                 q.append((ni, nj, grid[ni][nj] + v))
        return max(answer)