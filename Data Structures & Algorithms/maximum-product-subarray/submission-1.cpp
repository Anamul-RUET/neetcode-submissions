class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mx=1,mn=1,ans=INT_MIN;
        for(int i=0;i<nums.size();i++){
            mx*=nums[i];
            mn*=nums[i];
            ans=max(ans,mx);
            ans=max(ans,mn);
            if(mx<=0) mx=1;
            if(mn==0) mn=1;
        }
        mx=1,mn=1;
        reverse(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            mx*=nums[i];
            mn*=nums[i];
            ans=max(ans,mx);
            ans=max(ans,mn);
            if(mx<=0) mx=1;
            if(mn==0) mn=1;
        }
        return ans;
    }
};
