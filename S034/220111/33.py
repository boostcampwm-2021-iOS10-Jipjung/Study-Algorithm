from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] > nums[i + 1]:
                break
            i += 1
            
        left = bisect_left(nums, target, 0, i)
        right = bisect_left(nums, target, i + 1, len(nums) - 1)
        
        if left < n:
            if nums[left] == target:
                return left
        if right < n:
            if nums[right] == target:
                return right
        return -1
        