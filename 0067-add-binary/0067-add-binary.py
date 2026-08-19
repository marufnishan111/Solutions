class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y=0,0
        for i in a:
            x=(x<<1) | (i=='1')
        for i in b:
            y=(y<<1) | (i=='1')
        
        while y:
            c=(x&y)<<1
            x^=y
            y=c
        return bin(x)[2:]
        