class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

        stg = ''

        for i in s:
            if i in words:
                stg += i.lower()
        
        return (stg == stg[::-1])