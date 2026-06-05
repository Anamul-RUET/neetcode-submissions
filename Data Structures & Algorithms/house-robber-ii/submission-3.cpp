class Solution {
public:
    int func(vector<int>&nums,int l,int r){
         int dp[101];
       dp[l]=nums[l];
       if (r - l <= 1)
            return dp[l];
       dp[l+1]=max(nums[l],nums[l+1]);
       for(int i=l+2;i<r;i++){
       dp[i]=max(dp[i-1],(i-2>=0)?(dp[i-2] +nums[i]):nums[i]);
       }
       return dp[r-1];
    }
    int rob(vector<int>& nums) {
        int n=nums.size();
        if(n==1) return nums[0];
        return max(
            func(nums,0,n-1),func(nums,1,n)
        );
    }
};
