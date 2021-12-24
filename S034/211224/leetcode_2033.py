# discussion을 보면서 풀었던 문제, 쉬운데 까다롭다. 다시보면 좋을 듯
# 중간 값으로 부터의 거리로 계산하는 건데 증명을 하지 못하면 절대 못풀 듯
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr += row
        median = sorted(arr)[len(arr) // 2]
        answer = 0
        for integer in arr:
            diff = abs(median - integer)
            if diff % x != 0:
                return -1
            answer += (diff // x)
        return answer