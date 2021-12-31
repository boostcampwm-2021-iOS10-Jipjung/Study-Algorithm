class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        opers = []
        nums = []
        for i in range(0, len(s), 2):
            nums.append(int(s[i]))
        for i in range(1, len(s), 2):
            opers.append((lambda x, y: x + y) if s[i] == "+" else (lambda x, y: x * y))
        dp = [[set() for i in range(len(nums))] for i in range(len(nums))]
        for i, v in enumerate(nums):
            dp[i][i].add(v)

        for j in range(1, len(nums)):            
            for i in range(j - 1, -1, -1):
                temp_i = j
                temp_j = j - 1
                while temp_i > i:
                    dp[i][j] = dp[i][j].union(self._calculator(dp[temp_i][j], opers[temp_j], dp[i][temp_j]))
                    temp_i -= 1
                    temp_j -= 1
        score = 0
        precise_answer = eval(s)
        for answer in answers:
            if precise_answer == answer:
                score += 5
            elif answer in dp[0][-1]:
                score += 2
        return score

    def _calculator(self, set1, oper, set2):
        new_set = set()
        for i in set1:
            for j in set2:
                res = oper(i, j)
                if res <= 1000:
                    new_set.add(res)
        return new_set