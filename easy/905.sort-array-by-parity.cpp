// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {

     // O(n)

     int l = 0;
     int r = nums.size() - 1;

     while (l < r) {
       if (nums[l] % 2 != 0 && nums[r] % 2 == 0) {
         swap(nums[l], nums[r]);
         l++;
         r--;
       }
       if (nums[l] % 2 == 0) {
         l++;
       }
       if (nums[r] % 2 != 0) {
         r--;
       }
     }

     return nums;
    }
};
// @leet end
