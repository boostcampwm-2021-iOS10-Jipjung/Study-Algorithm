# 7분 단순 set과 counter를 이용해서 계산하였음

from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = []
        set1 = set(nums1)
        nums += list(set1)
        set2 = set(nums2)
        nums += list(set2)
        set3 = set(nums3)
        nums += list(set3)
        counter = Counter(nums)
        
        return list(map(lambda x: x[0], filter(lambda x: x[1] >= 2, counter.items())))