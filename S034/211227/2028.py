class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        sum_n_rolls = total - sum(rolls)
        if sum_n_rolls > 6 * n or sum_n_rolls < n:
            return []
        answer = [1] * n
        remain = sum_n_rolls - n
        i = 0
        while remain > 5:
            answer[i] += 5
            i += 1
            remain -= 5
        answer[i] += remain
        return answer