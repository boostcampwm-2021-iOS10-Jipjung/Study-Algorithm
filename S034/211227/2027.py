class Solution:
    def minimumMoves(self, s: str) -> int:
        o_count = 0
        move = 0
        count = 0
        for i in range(len(s)):
            if count == 0 and s[i] == "O":
                continue
            count += 1
            if count == 3:
                move += 1
                count = 0
        if count > 0 and move > 0:
            move += 1
        return move