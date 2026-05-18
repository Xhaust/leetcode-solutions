// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int search(vector<int>& nums, int target) {

      // O(log n) | WATCHED SOLUTION

      int l = 0;
      int r = nums.size() - 1;

      while (l <= r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
          return mid;
        }
        if (nums[l] <= nums[mid]) {
          if (target < nums[mid] && target >= nums[l]) {
            r = mid - 1;
          } else {
            l = mid + 1;
          }
        } else {
          if (target > nums[mid] && target <= nums[r]) {
            l = mid + 1;
          } else {
            r = mid - 1;
          }
        }
      }
      return -1;
    }
};
// @leet end
