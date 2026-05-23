class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            frequencies = {}
            freq={}
            for char in s:
                frequencies[char] = frequencies.get(char, 0) + 1
            for char in t:
                freq[char]=freq.get(char,0)+1
            if freq==frequencies:
                return True
            else:
                return False