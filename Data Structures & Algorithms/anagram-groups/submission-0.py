class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def a(s, t):
            frequencies = {}
            freq = {}

            for char in s:
                frequencies[char] = frequencies.get(char, 0) + 1

            for char in t:
                freq[char] = freq.get(char, 0) + 1

            return freq == frequencies

        l1 = []
        visited = set()

        for i in range(len(strs)):

            if i in visited:
                continue

            l2 = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(strs)):

                if j not in visited and a(strs[i], strs[j]):
                    l2.append(strs[j])
                    visited.add(j)

            l1.append(l2)

        return l1