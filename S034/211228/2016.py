# n^2 4분짜리 문제
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    result = max(result, nums[j] - nums[i])
        return result