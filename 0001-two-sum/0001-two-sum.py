class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=sorted(nums)
        l,r=0,len(m)-1
        while l<r:
            s = m[l]+m[r]
            if s==target:
                i=nums.index(m[l])
                j=nums.index(m[r], i+1) if m[l]==m[r] else nums.index(m[r])
                return [i,j]
            elif s<target:
                l+=1
            else:
                r-=1