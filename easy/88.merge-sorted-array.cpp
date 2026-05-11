// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

      //O(n+m)

      int l = m - 1;
      int r = m + n - 1;

      int j = n - 1;

      if (m == 0){
        nums1 = nums2;
        return;
      }

      if (n == 0){
        return;
      }

      while (l <= r) {
        if (nums1[l] <= nums2[j]) {
          nums1[r] = nums2[j];
          j--;
        } else {
          nums1[r] = nums1[l];
          nums1[l] = -109;
          if (l > 0){
            l--;
          }
        }
        if (j < 0){
          return;
        }
        r--;
      }
    }
};
// @leet end
