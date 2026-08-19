class Solution:
    def singleNumber(self, n: List[int]) -> int:
        x=n[0]
        for i in range(1,len(n)):
            x^=n[i]
        return x