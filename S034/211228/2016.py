class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        _max = -1
        _min = 1000000000 + 1
        for num in nums:
            if num < _min:
                _min = num
                _max = -1
            elif num > _min:
                if num > _max:
                    _max = num
                result = max(result, _max - _min)
        return result