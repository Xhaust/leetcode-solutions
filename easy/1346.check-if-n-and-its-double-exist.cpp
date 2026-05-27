// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {

      // O(n log n)

      sort(arr.begin(), arr.end());

      for (int i = 0; i < arr.size(); i++) {
        int target = arr[i] * 2;
        int l = 0;
        int r = arr.size() - 1;
        while (l <= r) {
          int mid = l + (r - l) / 2;
          if (target == arr[mid] || mid != i) {
            return true;
          } else if (target < arr[mid]) {
            r = mid - 1;
          } else {
            l = mid + 1;
          }
        }
      }
      return false;
    }
};
// @leet end
