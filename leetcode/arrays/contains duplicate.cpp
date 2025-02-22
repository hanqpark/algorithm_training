class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> m;

        for (const auto &n: nums) {
            if (m[n]++) return true;
        }

        return false;
    }
};
