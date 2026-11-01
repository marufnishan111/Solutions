class Solution:
    def minMoves(self, n: list[int]) -> int:
        return sum(n)-len(n)*min(n)