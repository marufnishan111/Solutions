class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        while len(s)>1:
            d=0
            for i in s:
                d+=int(i)
            s=str(d)
        return int(s)