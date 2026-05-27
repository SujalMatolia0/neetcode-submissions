class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a = set(nums)
        longest = 0

        for i in a:

            if i - 1 not in a:

                count = 1
                current = i

                while current + 1 in a:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest