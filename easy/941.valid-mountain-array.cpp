// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {

      // O(n)

      /// FIRST APPROACH
      //
      // if (arr.size() < 3) {
      //   return false;
      // }
      //
      // bool peakReached = false;
      // int peak = 0;
      // for (int i = 1; i < arr.size(); i++) {
      //   if (arr[i] < arr[i - 1] && peakReached == false) {
      //     if (arr[i] != arr.size() - 1) {
      //       peakReached = true;
      //       peak = arr[i - 1];
      //     }
      //   } else if ((arr[i] > arr[i - 1] || peak == arr[i]) && peakReached == true) {
      //     return false;
      //   }
      // }
      // if (peakReached == false) {
      //   return false;
      // } else {
      //   return true;
      // }
      //
      // SECOND APPROACH
      //
      // int l = 1;
      // int r = arr.size() - 2;
      //
      // while (l < r) {
      //   if (arr[l - 1] > arr[l] || arr[r + 1] < arr[r]) {
      //     return false;
      //   }
      //   r--;
      //   l++;
      // }
      // return true;
      //
      //
      // THIRD APPROACH
      //
      // if (arr.size() < 3) {
      //   return false;
      // }
      // int i = 1;
      // while (arr[i] > arr[i-1]) {
      //   i++;
      // }
      // while (arr[i] < arr[i-1]) {
      //   i++;
      // }
      //
      // if (i == arr.size() - 1) {
      //   return true;
      // } else return false;

      // FOURTH APPROACH
     
      if (arr.size() < 3) {
        return false;
      }
      
      bool peakReached = false;
      for (int i = 1; i < arr.size(); i++) {
        if (arr[i] == arr[i-1]) {
          return false;
        }
        if (arr[i] < arr[i-1]) {
          peakReached = true;
        }
        if (peakReached == true && arr[i] >= arr[i-1]) {
          return false;
        }
      }
      if (peakReached != true || arr[0] > arr[1]) {
        return false;
      }
      return true;
    }
};
// @leet end
