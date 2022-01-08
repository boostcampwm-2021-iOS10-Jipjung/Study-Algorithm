class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        count = 1
        n = len(nextVisit)
        dp = [0] * n
        mod = 1e9 + 7
        
        for i in range(1, n):
            dp[i] = (dp[i - 1] * 2 - dp[nextVisit[i - 1]] + 2) % mod
        return int(dp[i])
        