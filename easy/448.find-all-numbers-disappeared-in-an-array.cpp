// @leet imports start
#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {

      // O(n)

      unordered_set<int> completeList;
      vector<int> res;

      for (int i = 1; i <= nums.size(); i++) {
        completeList.insert(i);
      }

      for (int i = 0; i < nums.size(); i++) {
        completeList.erase(nums[i]);
      }

      for (int num : completeList) {
        res.push_back(num);
      }
      return res;
    }
};
// @leet end
