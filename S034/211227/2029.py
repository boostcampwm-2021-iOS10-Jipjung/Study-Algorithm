from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remains = collections.Counter(a % 3 for a in stones)
        if min(remains[1], remains[2]) == 0:
            return max(remains[1], remains[2]) > 2 and remains[0] % 2 > 0
        return abs(remains[1] - remains[2]) > 2 or remains[0] % 2 == 0
            