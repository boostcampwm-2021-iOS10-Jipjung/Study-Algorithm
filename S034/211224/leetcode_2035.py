from itertools import combinations
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        lefts, rights = nums[:n], nums[n:]
        left_sum, right_sum = sum(lefts), sum(rights)
        ans = abs(left_sum - right_sum)
        
        for i in range(1, n):
            left_diffs = sorted(sum(comb) * 2 - left_sum for comb in combinations(lefts, i))
            for right_diff in map(lambda comb: sum(comb) * 2 - right_sum, combinations(rights, i)):
                index = bisect_left(left_diffs, right_diff, 0, len(left_diffs) - 1)
                ans = min(ans, abs(left_diffs[index] - right_diff))
        return ans