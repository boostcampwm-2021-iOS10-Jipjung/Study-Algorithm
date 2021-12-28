class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        bottom_route = 0
        top_route = sum(grid[0]) - grid[0][0]
        answer = top_route
        for j in range(1, len(grid[0])):
            top_route -= grid[0][j]
            bottom_route += grid[1][j - 1]
            answer = min(answer, max(top_route, bottom_route))   
        return answer