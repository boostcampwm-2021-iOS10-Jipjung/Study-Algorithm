# 2가지의 기준으로 정렬된 배열을 조건에 맞게 비교해서 세는 문제. (dp)

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        maxValue = 0
        ans = 0
        for element in properties:
            if element[1] < maxValue:
                ans += 1
            else:
                maxValue = element[1]
        return ans
