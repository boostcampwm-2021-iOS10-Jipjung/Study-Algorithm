class Solution:
    def minimumMoves(self, s: str) -> int:
        cur = 0
        ans = 0
        length = len(s)
        while cur < length:
            if s[cur] == "X":
                cur += 3
                ans += 1
            else:
                cur += 1
        return ans