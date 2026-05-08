// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int findNumbers(vector<int>& nums) {
      int ans = 0;
      float curr = 0;
      int digits = 0;
      for (int& num : nums) {
        curr = num;
        while (curr >= 1) {
          curr = curr / 10;
          digits++;
        }
        if (digits % 2 == 0) {
          ans++;
        }
        digits = 0;
      }
      return ans;
    }
};
// @leet end
