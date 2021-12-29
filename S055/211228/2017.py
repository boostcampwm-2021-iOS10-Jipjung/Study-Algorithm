# top, bottom을 나누어서 2가지 경우에 대해서만 비교 

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum = sum(grid[0])
        bottomSum = 0
        ans = 0
        for i in range(grid[0]):
            topSum -= grid[i]
            ans = min(ans, bottomSum)
            bottomSum += grid[i]
        return ans