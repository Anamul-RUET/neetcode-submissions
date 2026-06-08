class Solution:
    def getSum(self, a: int, b: int) -> int:
        curr=0
        ans=0
        mask = 0xFFF
        for i in range(0,12):
            val = ((a >> i) & 1) + ((b >> i) & 1) + curr
            if(val==3):
              ans|=(1<<i)
              curr=1
            elif(val==2): curr=1
            elif(val==1):
                 ans|=(1<<i)
                 curr=0
            else: curr=0
        return ans if ans <= 0x7FF else ~(ans ^ mask)