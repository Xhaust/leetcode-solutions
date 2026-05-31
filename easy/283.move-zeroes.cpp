// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
      // O(n)
      
      int l = 0;

      for (int r = 0; r < nums.size(); r++) {
        if (nums[r] != 0) {
          nums[l] = nums[r];
          if (l != r) {
            nums[r] = 0;
          }
          l++;
        }
      }
    }
};
// @leet end
