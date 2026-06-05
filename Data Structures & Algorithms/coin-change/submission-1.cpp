class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount==0) return 0;
        vector<int>dp(amount+1,INT_MAX);
        int n=coins.size();
        for(int i=1;i<=amount;i++){
           for(int j=0;j<n;j++){
            if(i-coins[j]==0) dp[i]=1;
            else{
                if(i-coins[j]>0){
                  if(dp[i-coins[j]]!=INT_MAX){
                    dp[i]=min(dp[i],dp[i-coins[j]]+1);
                  }
                }
            }
           }
        }
        if(dp[amount]==INT_MAX) return -1;
        else return dp[amount];
    }
};
