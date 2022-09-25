// #include <bits/stdc++.h>
// using namespace std;

// class Solution {
// public:
//     vector<int> goodIndices(vector<int>& nums, int k) {
//         vector<int> nonIncrease{};
//         vector<int> nonDecrease{};
//         int n=nums.size();
//         vector<int> result;
//         int count=1;
//         if(k==1){
//             for(int i=1;i<n-1;i++){
//                 result.push_back(i);
//             }
//             return result;
//         }
//         if(k==1){
//             nonIncrease.push_back(1);
//         }
//         else{
//             nonIncrease.push_back(0);
//         }
        
//         for(int i=1;i<n;i++){
//             if(nums[i]>nums[i-1]){
//                 nonIncrease.push_back(0);
//                 count=1;
//             }
//             else{
//                 count+=1;
//                 if(count>=k){
//                     nonIncrease.push_back(1);
//                 }
//                 else{
//                     nonIncrease.push_back(0);
//                 }
//             }
//         }
        
        
//         if(k==1){
//             nonDecrease.insert(nonDecrease.begin(),1);
//         }
//         else{
//             nonDecrease.insert(nonDecrease.begin(),0);
//         }
//         count=1;
//         for(int i=n-1;i>=1;i--){
//             if(nums[i]<nums[i-1]){
//                 nonDecrease.insert(nonDecrease.begin(),0);
//                 count=1;
//             }
//             else{
//                 count+=1;
//                 if(count>=k){
//                     nonDecrease.insert(nonDecrease.begin(),1);
//                 }
//                 else{
//                     nonDecrease.insert(nonDecrease.begin(),0);
//                 }
//             }
//         }
        
        
//         for(int i=0;i<n-2;i++){
//             if(nonIncrease[i]&&nonDecrease[i+2]){
//                 result.push_back(i+1);
//             }
//         }
//         return result;
//     }
// };


// probably delay of insert function
// O(2n) is ok



class Solution {
public:
    vector<int> goodIndices(vector<int>& nums, int k) {
        int n = nums.size();
        
        vector<int> left(n,0) , right(n,0);
        
        for(int i = 1; i < n ; i++){
            if(nums[i] <= nums[i-1]){
                left[i] = left[i-1]+1;
            }
        }
        for(int i = n-2 ; i>= 0 ; i--){
            if(nums[i] <= nums[i+1]){
                right[i] = right[i+1]+1;
            }
        }
        vector<int> ans;
        
        for(int i = k ; i< n-k ; i++){
            if(min(left[i-1],right[i+1]) >= k-1){
                ans.push_back(i);
            }
        }
        return ans;
    }
};

