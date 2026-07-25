class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1=sum(nums)
        s=""
        for i in nums:
            s+=str(i)
        x=0
        for i in s:
            x+=int(i)
        return sum1-x