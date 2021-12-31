import heapq

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        minq = []
        maxq = [(-nums[0], 0)]
        answer = 0
        
        for i in range(2, len(nums)):
            heapq.heappush(minq, (nums[i], i))
            
        for i in range(1, len(nums) - 1):
            while minq and i >= minq[0][1]:
                heapq.heappop(minq)
            if -maxq[0][0] < nums[i] < minq[0][0]:
                answer += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                answer += 1
            heapq.heappush(maxq, (-nums[i], i))
        return answer 
            