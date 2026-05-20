// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
      
      //O(log n)

      if (nums.size() == 1) {
        return 0;
      }

      int l = 1;
      int r = nums.size() - 1;

      while (l < r) {
        int mid = l + (r - l) / 2;

        if (nums[mid - 1] < nums[mid] && nums[mid + 1] < nums[mid]) {
          return mid;
        } else if (nums[mid - 1] > nums [mid]) {
          r = mid;
        } else {
          l = mid + 1;
        }
      }
      if (nums[l - 1] > nums[r]){
        return l -  1;
      } else {
        return l;
      }
    }
};
// @leet end
