// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
      // FIRST ATTEMPT: O(n^2)
      //
      // int n = arr.size();
      // for (int i = 0; i < n; i++) {
      //   if (arr[i] == 0) {
      //     for (int j = n - 1; j >= i; j--) {
      //       if (j + 1 < n) {
      //         arr[j + 1] = arr[j];
      //       }
      //     }
      //     if (i + 1 < n){
      //       arr[i + 1] = 0;
      //       i++;
      //     }
      //   }
      // }

      // SECOND ATTEMPT: O(n)

      int zeros = 0;
      int n = arr.size();

      for (int num : arr){
        if (num == 0) {
          zeros++;
        }
      }

      int l = n - 1;
      int r = n + zeros - 1;

      while (l < r) {
        if (r < n){
          arr[r] = arr[l];
        }

        if (arr[l] == 0) {
          r--;
          if (r < n) {
            arr[r] = 0;
          }
        }

        l--;
        r--;
      }
    }
};
// @leet end
