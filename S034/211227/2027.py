class Solution:
    def minimumMoves(self, s: str) -> int:
        o_count = 0
        move = 0
        before_index = -1
        for i in range(len(s)):
            if s[i] == "O":
                o_count += 1
            if i - before_index == 3:
                if o_count < 3:
                    move += 1
                before_index = i
                o_count = 0
            if i == len(s) - 1 and i - before_index > o_count:
                move += 1
        return move