// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

      // FIRST ATTEMPT: WRONG
      //
      // int n = nums.size();
      //
      // int j = 0;
      // int k = 0;
      //
      // int l = -1;
      // int r = n - 1;
      //
      // for (int i = 0; i < n; i++) {
      //   if (nums[i] == -1) {
      //     return k;
      //   }
      //
      //   if (nums[i] == val) {
      //     if (nums[r] == val) {
      //       nums[i] = -1;
      //       nums[r] = nums[i];
      //       l = i;
      //       j++;
      //     } else {
      //       nums[i] = -1;
      //       nums[i] = nums[r];
      //       nums[r] = -1;
      //       k++;
      //     }
      //     r--;
      //   } else {
      //     if (j > 0){
      //       nums[l] = nums[i];
      //       nums[i] = nums[r];
      //       l--;
      //       j--;
      //     }
      //     k++;
      //   }
      // }
      // return k;

      // SECOND ATTEMPT: n(0)

      int n = nums.size();
      int k = 0;

      int l = 0;
      int r = n - 1;

      while (l <= r) {
        if (nums[l] != val) {
          k++;
          l++;
        } else {
          if (nums[r] != val) {
            nums[l] = nums[r];
          }
          r--;
        }
      }
      return k;
    }
};
// @leet end
