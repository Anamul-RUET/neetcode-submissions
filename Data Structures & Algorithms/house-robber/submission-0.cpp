class Solution {
public:
    int rob(vector<int>& nums) {
       int dp[101];
       dp[0]=nums[0];
       int n=nums.size();
       for(int i=1;i<n;i++){
       dp[i]=max(dp[i-1],(i-2>=0)?(dp[i-2] +nums[i]):nums[i]);
       }
       return dp[n-1];
    }
};
