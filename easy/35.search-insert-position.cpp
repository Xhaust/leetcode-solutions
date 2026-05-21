// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

      // O(log n)
      
      int l = 0;
      int r = nums.size() - 1;

      while (l <= r) {

        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
          return mid;
        } else if (nums[mid] > target) {
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
      return l; 
    }
};
// @leet end
