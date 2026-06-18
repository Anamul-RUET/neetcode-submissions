class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            tmp=len(i)
            res+=str(tmp)+"#"+i
        return res 

    def decode(self, s: str) -> List[str]:
        v=[]
        i=0
        while i<len(s):
           j=i
           while(s[j]!='#'):
            j+=1
           val=int(s[i:j])
           v.append(s[j+1:val+j+1])
           i=val+j+1
        return v

