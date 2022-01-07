from collections import defaultdict
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        edges = defaultdict(list)
        for i, parent in enumerate(parents):
            edges[parent].append(i)
        
        genetics = [i for i in range(100002)]
        answer = [1 for i in range(len(parents))]
        def dfs(here):
            if genetics[nums[here]] == 0:
                return
            for there in edges[here]:
                dfs(there)
            genetics[nums[here]] = 0

        value_index = 1
        if 1 not in nums:
            return answer
        node_index = nums.index(1)
        while node_index >= 0:
            dfs(node_index)
            while genetics[value_index] == 0:
                value_index += 1
            answer[node_index] = value_index
            node_index = parents[node_index]
        return answer