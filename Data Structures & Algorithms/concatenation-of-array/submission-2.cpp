class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> res;
        int l = nums.size();

        for (auto i = 0; i < (l * 2); i++)
        {
            res.push_back(nums[i % l]);
        }

        return res;
    }
};