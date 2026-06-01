// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

      // O(n)

      for (int i = digits.size() -1; i >= 0; i--) {
        if (digits[i] < 9) {
          digits[i]++;
          return digits;
        } else {
          digits[i] = 0;
        }
      }
      digits.insert(digits.begin(), 1);
      return digits;
    }
};
// @leet end
