class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            res = target - num
            if res in d:
                return [d[res], i]
            else:
                d[num] = i