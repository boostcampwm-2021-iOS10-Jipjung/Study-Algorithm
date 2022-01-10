class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        i = 0
        j = k - 1
        answer = sorted_nums[j] - sorted_nums[i]
        while j < len(nums):
            answer = min(answer, sorted_nums[j] - sorted_nums[i])
            i += 1
            j += 1
        return answer