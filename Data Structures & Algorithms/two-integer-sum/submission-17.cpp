class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        std::vector<int> res;

        for (size_t i = 0; i < nums.size(); i++)
        {
            int need = target - nums[i];
            if (seen.contains(need))
            {
                res.push_back(seen[need]);
                res.push_back(i);
                return res;
            }
            else
            {
                seen[nums[i]] = i;
            }
        }
        
    }
};
