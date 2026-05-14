// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int search(vector<int>& nums, int target) {
    //   FIRST ATTEMPT: WRONG
    //
    //   int l = 0;
    //   int r = nums.size() - 1;
    //   int mid = r / 2;
    //
    //   while (mid != l && mid != r) {
    //     if (target < nums[mid]) {
    //       r = mid;
    //       mid = r / 2;
    //     } else if (target > nums[mid]) {
    //       l = mid;
    //       mid += (r - l) / 2;
    //     } else {
    //       return mid;
    //     }
    //   }
    //   return -1;
    //
    
    //   SECOND ATTEMPT: O(log n)
    
      int l = 0;
      int r = nums.size() - 1;

      while (l <= r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
          return mid;
        }

        if (target < nums[mid]) {
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
      return -1;
    }
};
// @leet end
