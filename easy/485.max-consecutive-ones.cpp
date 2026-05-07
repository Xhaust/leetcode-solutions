// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
      int res = 0;
      int curr = 0;
      for (int i = 0; i < nums.size(); i++) {
        if (nums[i]) {
          curr++;
        } else {
          if (curr > res) {
            res = curr;
          }
          curr = 0;
        }
      }
      if (curr > res) {
        res = curr;
      }
      return res;
    }
};
// @leet end
