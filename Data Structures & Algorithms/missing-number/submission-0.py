class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in nums:
            ans^=i 
        for i in range(n+1):
            ans^=i
        return ans