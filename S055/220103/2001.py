# 처음에 사용한 방법으로 단순하게 2중 반복문을 돌아가며 확인하는 방법O(n^2)을 사용했고 TLE가 발생함.
# 두번째 사용한 방법은, 모든 원소들의 값의 갯수를 세고 nC2를 계산했음.
# Time Complexity O(n), Space Complexity O(n)

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dict = {}
        for element in rectangles:
            key = element[0] / element[1]
            if key not in dict:
                dict[key] = 1
            else:
                dict[key] += 1
        
        ans = 0
        for n in dict.values():
            if n < 1:
                continue
            ans += n*(n-1) // 2
        return ans
