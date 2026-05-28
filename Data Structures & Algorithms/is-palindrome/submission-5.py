class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

        o = ''

        for i in s:
            if i in a:
                o += i.lower()

        return o == o[::-1]