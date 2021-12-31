class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for operation in operations:
            if operation[0] == "+" or operation[-1] == "+":
                answer += 1
            else:
                answer -= 1
        return answer