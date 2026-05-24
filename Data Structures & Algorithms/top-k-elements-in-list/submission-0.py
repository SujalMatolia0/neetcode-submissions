class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        l1 = []

        for j in range(k):

            a = max(freq, key=freq.get)

            l1.append(a)

            del freq[a]

        return l1