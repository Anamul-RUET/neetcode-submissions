class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=set()
        for i in range(0,n):
            left=i+1
            right=n-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                if val==0 and i!=left and i!=right :
                    ans.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1

                elif(val>0):
                     right-=1
                else:
                    left+=1

        return [list(x) for x in ans]



        