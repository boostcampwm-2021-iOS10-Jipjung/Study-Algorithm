class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left_index = 0
        right_index = len(sorted_nums) // 2
        sums_nums = sum(sorted_nums)
        sums_subnums = sum(sorted_nums[:right_index])
        answer = abs(sums_nums - sums_subnums * 2)
        print(sums_nums, sums_subnums)
        while right_index < len(nums):
            print(answer)
            sums_subnums += -sorted_nums[left_index] + sorted_nums[right_index]
            answer = min(answer, abs(sums_nums - sums_subnums * 2))
            left_index += 1
            right_index += 1
        return answer