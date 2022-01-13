from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0 for i in range(len(nums))]
        q = deque()
        q.append((0, 0))
        visited = [False for i in range(len(nums))]
        visited[0] = True
        while q:
            here, jump = q.popleft()
            if here == len(nums) - 1:
                return jump
            for i in range(1, nums[here] + 1):
                if here + i >= len(nums) or visited[here + i]:
                    continue
                visited[here + i] = True
                q.append((here + i, jump + 1))