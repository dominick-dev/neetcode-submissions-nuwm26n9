class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++)
        {
            int need = target - nums.at(i);

            if (seen.contains(need))
            {
                return {seen[need], i};
            }

            seen[nums[i]] = i;
        }

        std::cout << "bad";
        return {};
    }
};
