// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {

        // O(log n)
      
        if (n == 1) {
          return n;
        }
        
        int l = 1;
        int r = n;

        while (l < r) {
          int mid = l + (r - l) / 2;

          if (isBadVersion(mid)) {
            r = mid;
          } else {
            l = mid + 1;
          }
        }
        
        if (!isBadVersion(l)) {
          return r;
        } else {
          return l;
        }
    }
};
// @leet end
