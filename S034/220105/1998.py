class Solution:
    def find(self, parent, x):
        if parent[x] < 0:
            return x
        # print(x, parent[x])
        return self.find(parent, parent[x])
    def union(self, parent, x, y):
        px, py = self.find(parent, x), self.find(parent, y)
        if px == py:
            return
        if parent[px] < parent[py]:
            parent[px] += parent[py]
            parent[py] = px
        elif parent[px] >= parent[py]:
            parent[py] += parent[px]
            parent[px] = py
    
    def gcdSort(self, nums: List[int]) -> bool:
        MAX = max(nums)
        sieve = [True] * (MAX + 1)
        nums_set = set(nums)
        sieve[0] = sieve[1] = False
        parent = [-1] * (MAX + 1)
        for i in range(2, MAX // 2 + 1):
            if not sieve[i]:
                continue
            j = i + i
            while j < len(sieve):
                if j in nums_set:
                    self.union(parent, i, j)
                sieve[j] = False
                j += i
                
        return all(self.find(parent, a) == self.find(parent, b) for a, b in zip(nums, sorted(nums)))