class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        for i in range(len(a)-2):
            if a[i]%2 and a[i+1]%2 and a[i+2]%2:
                return True
        return False