class Solution:
    def countBits(self, n: int) -> List[int]:
        vec=[]
        for i in range(0,n+1):
            cnt=0
            for j in range(0,11):
                if(i & 1<<j): cnt+=1
            vec.append(cnt)
        return vec
        