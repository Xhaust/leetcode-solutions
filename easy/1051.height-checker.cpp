// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int heightChecker(vector<int>& heights) {

      // O(n)

      vector<int> expected = heights;
      sort(expected.begin(), expected.end());
      int res = 0;

      for (int i = 0; i < heights.size(); i++) {
        if (heights[i] != expected[i]) {
          res++;
        }
      }
      return res;
    }
};
// @leet end
