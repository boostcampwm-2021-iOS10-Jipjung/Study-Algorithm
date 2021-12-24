class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for element in row:
                arr.append(element)
                
        arr.sort()
        
        length = len(grid[0]) * len(grid)
        mid = arr[length // 2]
        count = 0
        for element in arr:
            if not (element - mid) % x == 0: return -1
            count += abs(element - mid) // x
        return count
            
    
    