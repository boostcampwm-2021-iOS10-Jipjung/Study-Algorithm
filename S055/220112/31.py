# 추가 공간을 사용하지 않고 푸는 문제(제자리)였다. 파이썬의 range부분이 익숙하지 않아 실수를 많이 했다.
# Time: O(3*N) = O(N), Space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        target = 101
        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] < nums[i+1]: # 만약 현재꺼가 이전꺼보다 작다면, 오름차순이 깨짐
                target = i
                break
        
        if target == 101:
            nums.reverse()
            return
        
        # target보다 바로 다음단계로 큰 숫자를 찾고 target위치에 이동, 원래 target이 들어가 위치를 찾아서 넣기
        for i in reversed(range(target+1, len(nums))):
            if nums[i] > nums[target]:
                temp = nums[target]
                nums[target] = nums[i]
                nums[i] = temp
                break
                                     
        length = len(nums)-target-1
        for i in range(0, length // 2):
            temp = nums[i+target+1]
            nums[i+target+1] = nums[-1-i]
            nums[-1-i] = temp
