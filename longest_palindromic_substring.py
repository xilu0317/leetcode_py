class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for l in (self.expand(s, i, i), self.expand(s, i, i + 1)):
                if len(l) > len(res):
                    res = l
        return res
    def expand(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]