// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {

      // O(log n + k) || WATCHED SOLUTION

      // int l = 0;
      // int r = arr.size() - 1;
      // vector<int> ans(k);
      //
      // if (x <= arr[0]) {
      //   for (int i = 0; i < k; i++) {
      //     ans[i] = arr[i];
      //   }
      //   return ans;
      // }
      // if (x >= arr[r]) {
      //   for (int i = r; i < r - k; i--) {
      //     ans[i] = arr[i];
      //   }
      //   return ans;
      // }
      //
      // while (l + 1 < r) {
      //   int mid = l + (r - l) / 2;
      //   if (x - arr[l] <= arr[r] - x) {
      //     r = mid;
      //   } else {
      //     l = mid;
      //   }
      // }
      //
      //
      // for (int i = k; i > 0; i--) {
      //   if (x - arr[l] <= arr[r] - x && l > 0) {
      //     if (k == 1) {
      //       return {arr[l]};
      //     }
      //     l--;
      //   } else {
      //     if (k == 1) {
      //       return {arr[r]};
      //     }
      //     r++;
      //   }
      // }
      //
      // for (int i = l; i < k; i++) {
      //   ans[i] = arr[i];
      // }
      //
      // return ans;
      //
      int l = 0;
      int r = arr.size() - 1;

      while (l + 1 < r) {
        int mid = l + (r - l) / 2;

        if (arr[mid] < x) {
          l = mid;
        } else {
          r = mid;
        }
      }

      while (r - l - 1 < k ) {
        if (l < 0) {
          r++;
        } else if (r >= arr.size()) {
          l--;
        } else if (x - arr[l] <= arr[r] - x){
          l--;
        } else {
          r++;
        }
      }
      return vector<int>(arr.begin() + l + 1, arr.begin() + r);
    }
};
// @leet end
