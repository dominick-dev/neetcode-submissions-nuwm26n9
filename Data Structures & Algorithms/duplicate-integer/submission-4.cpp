class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> nums_set;

        for (auto num : nums)
        {
            if (nums_set.count(num))
            {
                return true;
            } 
            nums_set.insert(num);
        }

        return false;
    }
};