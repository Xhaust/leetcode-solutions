// @leet imports start
#include <bits/stdc++.h>
#include <vector>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
      // FIRST ATTEMPT: O(n^2)
      //
      // vector<int> ans(nums.size());
      // for (int i = 0; i < nums.size(); i++){
      //   ans[i] = nums[i] * nums[i];
      // }
      // for (int i = 0; i < ans.size(); i++){
      //   int temp = 0;
      //   for (int j = i; j < ans.size(); j++){
      //     if (ans[j] < ans[i]){
      //       temp = ans[i];
      //       ans[i] = ans[j];
      //       ans[j] = temp;
      //     }
      //   }
      // }
      // return ans;


      // SECOND ATTEMPT: O(n) (after learning two pointer algorithm)

      int n = nums.size();
      vector<int> ans(n);

      int left = 0;
      int right = n-1;

      for (int i = n-1; i >= 0; i--){
        if (abs(nums[right]) > abs(nums[left])){
          ans[i] = nums[right] * nums[right];
          right--; 
        } else {
          ans[i] = nums[left] * nums[left];
          left++; 
        }
      }
      return ans;
    }
};
// @leet end
