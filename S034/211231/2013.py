from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.grid = [[0 for i in range(1001)] for i in range(1001)]
        self.x = defaultdict(list)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].append(y)
        self.grid[x][y] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for j in self.x[x]:
            length = abs(y - j)
            if length == 0:
                continue
            for i in [x - length, x + length]:
                if i > 1000 or i < 0:
                    continue
                result += self.grid[i][y] * self.grid[i][j]
        return result