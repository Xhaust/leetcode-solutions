// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int findMin(vector<int>& nums) {

      // O(log n)
        
      if (nums.size() == 1) {
        return nums[0];
      }

      int l = 0;
      int r = nums.size() - 1;
      int lowest = 0;

      // while (l < r) {
      //   int mid = l + (r - l) / 2;
      //   if (nums[mid] < nums[l] && nums[mid] < nums[r]) {
      //     return nums[mid];
      //   } else if (nums[l] < nums[r]) {
      //     r = mid;
      //     lowest = nums[l];
      //   } else if (nums[r] < nums[l]) {
      //     l = mid + 1;
      //     lowest = nums[r];
      //   }
      // }
      // if (nums[l] < lowest) {
      //   return nums[l];
      // } else {
      //   return lowest;
      // }
      //

      while (l < r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] > nums[r]) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }

      return nums[l];
    }
};
// @leet end
