class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (len(rolls) + n) * mean
        value = total - sum(rolls)
        
        if not (n <= value <= 6*n):
            return []
        ans = [1]*n
        remain = value - n
        
        i = 0
        while remain > 5:
            ans[i] += 5
            remain -= 5
            i+=1
        ans[i] += remain
        return ans