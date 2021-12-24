from collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c1 = set(nums1)
        c2 = set(nums2)
        c3 = set(nums3)
        total = Counter(c1) + Counter(c2) + Counter(c3)
        return list(map(lambda x: x[0], filter(lambda x: x[1] > 1 , total.items())))