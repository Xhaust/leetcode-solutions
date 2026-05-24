// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
      
      // O(log n) | WATCHED SOLUTION
        
      // int l = 0;
      // int r = nums.size() - 1;
      // vector<int> ans = {-1, -1};
      //
      // while (l + 1 < r) {
      //   int mid = l + (r - l) / 2;
      //
      //   if (nums[mid] == target) {
      //     ans = {mid, mid};
      //     l = mid;
      //     r = mid;
      //   } else if (nums[mid] < target) {
      //     l = mid;
      //   } else {
      //     r = mid;
      //   }
      // }
      // while (nums[l] == target && l >= 0) {
      //   ans[0] = l;
      //   l--;
      // }
      // while (nums[r] == target && r < nums.size()) {
      //   ans[1] = r;
      //   r++;
      // }

      int l = 0;
      int r = nums.size() - 1;
      vector<int> ans(2, -1);

      while (l <= r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] < target) {
          l = mid + 1;
        } else {
          if (nums[mid] == target) {
            ans[0] = mid;
          }
          r = mid - 1;
        }
      }

      l = 0;
      r = nums.size() - 1;
      while (l <= r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] > target) {
          r = mid - 1;
        } else {
          if (nums[mid] == target) {
            ans[1] = mid;
          }
          l = mid + 1;
        }
      }
      return ans;
    }
};
// @leet end
