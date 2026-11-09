class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> res;
        int l = nums.size();
        res.resize(l * 2);

        for (auto i = 0; i < l; i++)
        {
            res[i] = nums[i];
            res[i + l] = nums[i];
        }

        return res;
    }
};