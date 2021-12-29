class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # O(nlogn + n) >> O(nlogn)
        _min = [nums[0]]
        _max = [-1]
        for element in nums:
            if _min[-1] > element:
                _min.append(element)
                _max.append(-1)
            else:
                if _max[-1] < element:
                    _max[-1] = element
        diff = [_max[i] - _min[i] for i in range(len(_max))]
        diff.sort(reverse=True)
        
        return diff[0] if diff[0] > 0 else -1
        