from collections import Counter
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = map(lambda x: x[0] / x[1], rectangles)
        answer = 0

        for ratio, count in Counter(ratios).items():
            if count < 2:
                continue
            answer += count * (count - 1) // 2
        return answer