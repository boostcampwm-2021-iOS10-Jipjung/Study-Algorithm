from itertools import combinations

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        n = len(nums) // 2
        n_combinations = combinations(nums, n)
        answer = sum(map(abs, nums))
        for combination in n_combinations:
            answer = min(answer, abs(sum_nums - 2 * sum(combination)))
        return answer