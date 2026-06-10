class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        vec=[]
        n=len(s)
        ans=0
        for i in range(0,n):
            if(s[i] in st):
                while vec[0]!=s[i]:
                      st.remove(vec[0])
                      vec.pop(0)
                st.remove(s[i])
                vec.pop(0)
            
            st.add(s[i])
            vec.append(s[i])
            ans=max(ans,len(st))
        return ans

        