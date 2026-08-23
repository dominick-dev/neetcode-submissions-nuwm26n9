class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // key:num val:idx
        std::unordered_map<int, int> seen;

        for (int idx = 0; idx < std::size(nums); idx++)
        {
            int num = nums[idx];
            int need = target - num;

            if (seen.contains(need))
            {
                return vector<int> {seen[need], idx};
            }

            seen.emplace(num, idx);
        }

        return {};
    }
};
