class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:]
        x=str(x)

        x=x[::-1]
        if len(x)<32:
            x+=('0'*(32-len(x)))
        
        x=int(x,2)
        return x