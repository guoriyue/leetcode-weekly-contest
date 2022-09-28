class Solution {
public:
    bool validPartition(vector<int>& nums) {
        vector<int> dp;
        dp.push_back(0);
        int n=nums.size();
        if(n<2){
            return false;
        }
        else if(n==2){
            if(nums[0]==nums[1]){
                return true;
            }
            return false;
        }
        if(nums[0]==nums[1]){
            dp.push_back(1);
        }
        else{
            dp.push_back(0);
        }
        if(nums[0]==nums[1]&&nums[1]==nums[2]){
            dp.push_back(1);
        }
        else if(nums[0]+1==nums[1]&&nums[1]+1==nums[2]){
            dp.push_back(1);
        }
        else{
            dp.push_back(0);
        }
        
        for(int i=3;i<n;i++)
        {
            if(dp[i-2]==1&&nums[i-1]==nums[i]){
                dp.push_back(1);
            }
            else if(dp[i-3]==1&&nums[i-1]==nums[i]&&nums[i-1]==nums[i-2]){
                dp.push_back(1);
            }
            else if(dp[i-3]==1&&nums[i-1]+1==nums[i]&&nums[i-1]==nums[i-2]+1){
                dp.push_back(1);
            }
            else{
                dp.push_back(0);
            }
        }
        return dp[n-1];
    }
};
