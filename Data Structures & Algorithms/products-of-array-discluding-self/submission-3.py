from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l1 = []

        for i in range(len(nums)):

            result = prod(nums[:i]) * prod(nums[i+1:])

            l1.append(result)

        return l1