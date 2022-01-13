# 두번째 방법 (Greedy)
# 현재 구간의 끝(curEnd)까지 다음 구간의 끝을 찾는 과정을 반복한다.
# 현재 구간의 끝(curEnd)에 다다르면, 현재구간의 끝부터 다음 구간의 끝(curEnd ~ nextFarthest)의 비용을 갱신한다(step+=1)
# 구간의 시작에 비용을 더해주고 있으므로 마지막 1번은 빼야 정확한 비용이 계산된다. (for문의 -1한 부분)
# Time: O(N), Space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        curEnd = 0
        nextFarthest = 0
        
        for i in range(len(nums)-1):
            nextFarthest = max(nextFarthest, i+nums[i])
            if i == curEnd:
                step += 1
                curEnd = nextFarthest
            
        return step

# 첫번째 방법        
# Time: O(N^2), Space: O(N)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         cost = [1e4]*len(nums)
#         cost[0] = 0

#         for base in range(len(nums)):
#             for i in range(1, nums[base]+1):
#                 if base+i< len(nums) and cost[base]+1 < cost[base+i]:
#                     cost[base+i] = cost[base]+1

#         return cost[-1]