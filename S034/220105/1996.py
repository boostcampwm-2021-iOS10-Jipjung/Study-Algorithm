from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        new_before_defense = -1
        answer = 0
        defenses = defaultdict(list)
        for i, j in properties:
            defenses[i].append(j)
        
        for attack in sorted(defenses, reverse = True):
            before_defense = new_before_defense
            for defense in defenses[attack]:
                if defense < before_defense:
                    answer += 1
                new_before_defense = max(defense, new_before_defense)
        return answer


# 위는 비효율적인 방법이여서
# (-x[0],x[1])) 로 정리한 풀이를 보았음.
# 이 방식으로 정렬해서 max보다 값이 작으면 찾고자하는 결과임을 알 수 있고
# attack이 같을때는 이미 정렬로 그 문제를 해결하였다.