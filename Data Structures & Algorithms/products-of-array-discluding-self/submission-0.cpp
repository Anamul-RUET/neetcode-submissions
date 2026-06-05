class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    int n=nums.size();
    vector<int>pref(n+1,1),suff(n+1,1),ans(n);
    for(int i=0;i<n;i++){
        if(i-1>=0) pref[i]=pref[i-1]*nums[i-1];
    }
    for(int i=n-1;i>=0;i--){
        if(i+1<n) suff[i]=suff[i+1]*nums[i+1];
    }
    for(int i=0;i<n;i++) ans[i]=pref[i]*suff[i];
    return ans;
    }
};
