# 3분짜리 매우 쉬움
from itertools import combinations
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        answer = 0
        for a, b, c, d in combinations(nums, 4):
            answer += 1 if a + b + c == d else 0
        return answer