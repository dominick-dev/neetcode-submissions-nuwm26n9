class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> nums_set = {};

        for (auto num : nums)
        {
            if (nums_set.find(num) != nums_set.end())
            {
                return true;
            } 
            nums_set.insert(num);
        }

        return false;
    }
};