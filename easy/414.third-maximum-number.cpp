// @leet imports start
#include <bits/stdc++.h>
#include <functional>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int thirdMax(vector<int>& nums) {

      //O(nlogn), TIL sort() is O(nlogn)

      // sort(nums.rbegin(), nums.rend());
      // int res = 0;
      // int max = nums[0];
      // int unique = 1;
      //
      // for (int i = 1; i < nums.size(); i++) {
      //   if (nums[i] > max) {
      //     max = nums[i];
      //   }
      //   if (nums[i] != nums[i - 1]) {
      //     unique++;
      //   }
      //   if (unique == 3) {
      //     res = nums[i];
      //   }
      // } 
      // if (unique < 3) {
      //   return max;
      // } else return res;

      // O(n)

      priority_queue<int, vector<int>, greater<int>> top3;
      unordered_set<int> seen;
      for (int num : nums) {
        if (seen.count(num)) continue;
        seen.insert(num);
        top3.push(num);
        if (top3.size() > 3) {
          top3.pop();
        }
      }
      if (top3.size() < 3) {
        for (int i = 0; i < top3.size(); i++) {
          top3.pop();
        }
      }
      return top3.top();
    }
};
// @leet end
