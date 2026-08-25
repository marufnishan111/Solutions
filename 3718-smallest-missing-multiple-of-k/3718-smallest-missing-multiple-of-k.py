class Solution:
    def missingMultiple(self, n: List[int], k: int) -> int:
        x=k
        while x in n:
            x+=k
        return x