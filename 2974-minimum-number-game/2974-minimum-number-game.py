class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n=sorted(nums)
        for i in range(0,len(nums),2):
            n[i],n[i+1]=n[i+1],n[i]
        return n