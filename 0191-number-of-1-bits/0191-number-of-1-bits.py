class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        x=str(x)
        return x.count('1')