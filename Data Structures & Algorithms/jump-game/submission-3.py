class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        curr=nums[0]
        if curr==0 and n>1: return False
        for i in range(1,n-1):
           curr=max(curr-1,nums[i])
           if(curr<=0):
             return False
        return True    
        