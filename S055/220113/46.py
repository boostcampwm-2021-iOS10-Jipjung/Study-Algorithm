# 두번째 방법(첫번째 방법에서 Copy 부분을 줄임, DFS)
# Time: O(N!), Space: O(N!)
# 각 재귀 중에 path+[element] 와 같은 연산을 수행하는 것이 매우 비싸다.
# 두 개의 목록에 대해 + 작업을 수행할 때마다 새 메모리가 생성되기 때문.
# 대신 path.pop()을 수행하여 역추적을 수행하는 것이 더 효율적인 방법.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(nums, remains):
            if not remains:
                ans.append(path[:])
                return
            for element in remains:
                next_remains = remains[:]
                next_remains.remove(element)
                
                path.append(element)
                dfs(nums, next_remains)
                path.pop()
                
        dfs(nums, nums[:])
        
        return ans

# 첫번째 방법(Copy, DFS)
# Time: O(N!), Space: O(N!)
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ans = []
        
#         def dfs(nums, path, remains):
#             if not remains:
#                 ans.append(path)
#                 return
#             for element in remains:
#                 next_remains = remains[:]
#                 next_remains.remove(element)
                
#                 dfs(nums, path+[element], next_remains)
                
#         dfs(nums, [], nums[:])
        
#         return ans