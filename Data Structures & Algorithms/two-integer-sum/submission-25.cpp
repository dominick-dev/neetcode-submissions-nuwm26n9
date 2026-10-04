class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        seen.reserve(nums.size());

        for (size_t i = 0; i < nums.size(); i++)
        {
            int need = target - nums[i];

            if (auto it = seen.find(need); it != seen.end())
            {
                return {it->second, (int)i};
            }

            seen.emplace(nums[i], (int)i);
        }

        return {};
    }
};
