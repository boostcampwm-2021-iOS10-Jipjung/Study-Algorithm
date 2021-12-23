# 24분정도걸림 - 아이디어 ㅂ내는데 10분 - 구현 14분정도,
from itertools import combinations
from functools import reduce

class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        target_bit = self._bit_sum(nums)
        count = 0
        for i in range(len(nums) + 1):
            nums_combis = combinations(nums, i)
            for nums_combi in nums_combis:
                if self._bit_sum(nums_combi) == target_bit:
                    count += 1
        return count

    def _bit_sum(self, nums):
        return reduce(lambda acc, var: acc | var, nums, 0)

print(Solution().countMaxOrSubsets([3,1]))