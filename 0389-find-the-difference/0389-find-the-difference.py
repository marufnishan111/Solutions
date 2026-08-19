class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s+=t
        x=0
        for i in (s):
            x^=ord(i)
        return chr(x)