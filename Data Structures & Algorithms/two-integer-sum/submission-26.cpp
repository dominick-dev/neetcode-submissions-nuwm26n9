class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        seen.reserve(nums.size());

        for (int i = 0; i < (int)nums.size(); i++)
        {
            int need = target - nums[i];

            auto it = seen.find(need);
            if (it != seen.end())
            {
                return {it->second, i};
            }

            seen.emplace(nums[i], i);
        }

        return {};
    }
};
