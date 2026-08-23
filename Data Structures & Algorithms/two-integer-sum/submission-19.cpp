class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // key:num val:idx
        std::unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++)
        {
            int need = target - nums[i];

            if (seen.contains(need))
            {
                return vector<int> {seen[need], i};
            }

            seen.insert({nums[i], i});
        }

        return {};
    }
};
