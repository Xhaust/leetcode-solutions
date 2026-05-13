// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

      // O(n)

      int k = 0;
      int curr;

      for (int num : nums) {
        if (num != curr) {
          nums[k++] = num;
          curr = num;
        }
      }
      return k;
    }
};
// @leet end
