# O(n^4)을 써도 통과하는 문제였다.
# a+b+c=d를 a+b=d-c 로 바꾸어 배열의 뒤부터 탐색한다.
# 이전에 찾았던 결과가 현재 탐색중인 a+b의 결과에 영향을 준다.(dp)
# Time: O(n^2), Space: O(n)

from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        size = len(nums)
        
        for b in range(size-1, 0, -1):
            for a in range(b-1, -1, -1):
                ans += count[nums[a] + nums[b]]
            
            for x in range(size-1, b, -1):
                count[nums[x]-nums[b]] += 1
        return ans
