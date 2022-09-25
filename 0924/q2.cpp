class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int count=0;
        int maxx=-1;
        int con=0;
        int result=1;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(maxx<nums[i]){
                maxx=nums[i];
                count=1;
                con=1;
                result=1;
            }
            else if(maxx==nums[i]&&con==1){
                count+=1;
                result=max(result,count);
            }
            else if(maxx==nums[i]&&con==0){
                count=1;
                con=1;
            }
            else if(maxx>nums[i]){
                con=0;
                result=max(result,count);
            }
            // result=max(result,count);
        }
        return result;
    }
};
