class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        curr=prices[0]
        for i in prices:
            if(curr>i):
                curr=i
            else:
                ans=max(ans,i-curr)
        return ans