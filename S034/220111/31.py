class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j < n and nums[j] > nums[i - 1]:
                    j += 1                    
                nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
                for k in range((n - i) // 2):
                    nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]
                return 
            i -= 1
        nums.reverse()