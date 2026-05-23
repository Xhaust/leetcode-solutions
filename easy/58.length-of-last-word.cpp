// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int lengthOfLastWord(string s) {

      // O(n)

      int length = 0;
      bool counting = false;

      for (int i = s.length() - 1; i >= 0; i--) {
        if (s[i] != ' ') {
          counting = true;
          length++;
        } else if (counting) {
          break;
        }
      }
      return length;
    }
};
// @leet end
