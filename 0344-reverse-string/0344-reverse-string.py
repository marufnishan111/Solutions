class Solution:
    def reverseString(self, s: List[str]) -> None:
        x=""
        for i in s:
            x+=str(i)
        s[:]=x[::-1]
        return s