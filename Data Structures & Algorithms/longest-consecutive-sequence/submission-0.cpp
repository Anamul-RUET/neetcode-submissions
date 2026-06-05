class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
       map<int,int>mp;
       for(int i=0;i<nums.size();i++) mp[nums[i]]++;
       int cnt=0,ans=1;
       auto tmp=mp.begin();
       int prev=tmp->first;
       for(auto it:mp){
        if(prev==it.first or prev+1==it.first){
            cnt++;
            ans=max(ans,cnt);
            prev=it.first;
        }
        else{
            cnt=1;
            prev=it.first;

        }
       }
       return ans;
    }
  
};
