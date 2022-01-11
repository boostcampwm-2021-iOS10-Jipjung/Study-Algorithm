# 이진탐색 경계조건 따지기가 힘들었다. 다시 풀어볼 문제로 추가함
# Time: O(2*logN) = O(logN), Space: O(1)

class Solution:
    def bs(self, nums, left, right, target):
        while left<right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left if target == nums[left] else -1
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
            
        # left: 구간 탐색
        ans = self.bs(nums, left, len(nums)-1, target)
        if ans != -1:
            return ans
        
        # :left 구간 탐색
        ans = self.bs(nums, 0, left, target)
        if ans != -1:
            return ans
        
        return -1
