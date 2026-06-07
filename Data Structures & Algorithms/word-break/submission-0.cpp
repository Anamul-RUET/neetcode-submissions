class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
      vector<int>dp(202,0);
      dp[0]=1;
      unordered_set<string>st(wordDict.begin(),wordDict.end());
      int n=s.size();
      for(int i=1;i<=n;i++) {
      for(int j=0;j<i;j++){
        if(dp[j] and st.count(s.substr(j,i-j))) dp[i]=1;
      }
      }
      return (dp[n])?true:false; 
    }
};
