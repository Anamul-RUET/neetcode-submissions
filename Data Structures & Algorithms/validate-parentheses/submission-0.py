class Solution:
    def isValid(self, s: str) -> bool:
        v=[]
        for i in range(len(s)):
            if s[i]==')':
                if v and v[-1]=='(':
                    v.pop()
                else:
                    return False
            elif s[i]=='}':
                if v and v[-1]=='{':
                    v.pop()
                else:
                    return False
            elif s[i]==']':
                if v and v[-1]=='[':
                    v.pop()
                else:
                    return False
            else:
                v.append(s[i])  
        if not v:
            return True
        else:
            return False   
        
